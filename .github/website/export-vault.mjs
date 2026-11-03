// Injected into the headless Obsidian window (see publish-website.yml).
//
// Same job as the exporter's own docker/export-vault.mjs: enable the vault's plugins,
// enable "Webpage HTML Export" and export every note to /output. Differences:
//   - The vault is exported twice. TikZJax draws each diagram in the background (one TeX run
//     per diagram) and remembers the result, but the exporter copies a page as soon as it has
//     rendered, so after the first pass the diagrams are still loading spinners. In the second
//     pass every diagram comes straight from TikZJax's cache and the pages are complete.
//     (Only the second pass is kept; the output folder is emptied in between.)
//   - The MathJax fonts are written to the site. The exporter points the formulas' CSS at
//     site-lib/fonts/mathjax_*.woff but never saves those files, so without this step the
//     formulas fall back to a plain serif font.
//   - A failure is printed with its stack trace, and Obsidian is given a moment to flush its
//     console to the log before it is stopped, so a broken export explains itself.

console.log('[export-vault] starting');

(async () => {
	const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

	// ---- follow TikZJax's TeX runs through the lines it prints
	const tex = { started: 0, finished: 0, lastActivity: Date.now() };
	const originalLog = console.log;
	console.log = function (...args) {
		const text = typeof args[0] === 'string' ? args[0] : '';
		if (text.startsWith('This is e-TeX')) {
			tex.started++;
			tex.lastActivity = Date.now();
		} else if (text.startsWith('Output written on input.dvi')) {
			tex.finished++;
			tex.lastActivity = Date.now();
		} else if (/^(\(|\*\*entering|No file input|Transcript written|ABD:)/.test(text)) {
			tex.lastActivity = Date.now();
		}
		return originalLog.apply(this, args);
	};

	function countTikzCache() {
		return new Promise((resolve) => {
			const open = indexedDB.open('TikzJax');
			open.onerror = () => resolve('unknown');
			open.onsuccess = () => {
				const db = open.result;
				try {
					const count = db.transaction('svgImages').objectStore('svgImages').count();
					count.onsuccess = () => { db.close(); resolve(count.result); };
					count.onerror = () => { db.close(); resolve('unknown'); };
				} catch (error) {
					db.close();
					resolve('unknown (' + error + ')');
				}
			};
		});
	}

	async function waitForTikz() {
		const files = app.vault.getMarkdownFiles();
		let expected = false;
		for (const file of files) {
			if ((await app.vault.cachedRead(file)).includes('tikz')) { expected = true; break; }
		}
		if (!expected) return;

		const deadline = Date.now() + 240000;
		while (Date.now() < deadline) {
			const quiet = Date.now() - tex.lastActivity;
			if (tex.started > 0 && tex.started === tex.finished && quiet > 6000) break;
			await sleep(500);
		}
		console.log('[export-vault] TikZ runs started: ' + tex.started + ', finished: ' + tex.finished +
			', drawings cached: ' + (await countTikzCache()));
	}

	// Every chart (```chart, ```advanced-chart and dataviewjs window.renderChart) goes through
	// the Charts plugin's renderRaw. Keep each chart's Chart.js config on its block so the site
	// can draw it live (hover, light/dark), and draw it here without animation so the picture
	// the exporter takes as a fallback shows the final values, not a frame of the animation.
	function recordCharts() {
		const charts = this.app.plugins.plugins['obsidian-charts'];
		if (!charts || !charts.renderer) {
			console.log('[export-vault] Charts plugin not loaded, charts stay pictures');
			return;
		}
		const original = charts.renderer.renderRaw.bind(charts.renderer);
		const recorded = function (data, el) {
			try {
				const config = data && data.chartOptions ? data.chartOptions : data;
				const style = getComputedStyle(el);
				el.setAttribute('data-chart-config', JSON.stringify(config));
				el.setAttribute('data-chart-theme', JSON.stringify({
					border: style.getPropertyValue('--background-modifier-border').trim(),
				}));
				if (config && typeof config === 'object') {
					config.options = config.options || {};
					config.options.animation = false;
				}
			} catch (error) {
				console.error('[export-vault] could not record a chart: ' + error);
			}
			return original(data, el);
		};
		charts.renderer.renderRaw = recorded;
		window.renderChart = recorded;
		console.log('[export-vault] recording chart configs');
	}

	async function writeMathJaxFonts() {
		const fs = require('node:fs');
		const path = require('node:path');
		const sheet = Array.from(document.styleSheets).find(
			(s) => s.ownerNode && s.ownerNode.id === 'MJX-CHTML-styles'
		);
		if (!sheet) {
			console.error('[export-vault] MathJax stylesheet not found, no fonts written');
			return;
		}
		const outDir = '/output/site-lib/fonts';
		fs.mkdirSync(outDir, { recursive: true });
		const done = new Set();
		for (const rule of Array.from(sheet.cssRules)) {
			if (rule.type !== CSSRule.FONT_FACE_RULE) continue;
			const src = rule.style.getPropertyValue('src');
			for (const match of src.matchAll(/url\(["']?([^"')]+)["']?\)/g)) {
				const url = match[1];
				// The exported pages ask for lower-case names (mathjax_main-regular.woff).
				const name = decodeURIComponent(url.split('?')[0].split('/').pop()).toLowerCase();
				if (done.has(name)) continue;
				done.add(name);
				try {
					const response = await fetch(url);
					if (!response.ok) throw new Error('HTTP ' + response.status);
					fs.writeFileSync(path.join(outDir, name), Buffer.from(await response.arrayBuffer()));
				} catch (error) {
					console.error('[export-vault] could not save font ' + url + ': ' + error);
				}
			}
		}
		console.log('[export-vault] MathJax fonts written: ' + done.size);
	}

	try {
		console.log('[export-vault] enabling community plugins');
		await this.app.plugins.setEnable(true);
		recordCharts.call(this);

		console.log('[export-vault] enabling Webpage HTML Export');
		await this.app.plugins.enablePlugin('webpage-html-export');
		const plugin = await this.app.plugins.getPlugin('webpage-html-export');
		if (!plugin) throw new Error('Webpage HTML Export did not load');

		console.log('[export-vault] export pass 1 of 2: draws the diagrams');
		await plugin.exportDocker();

		console.log('[export-vault] waiting for the diagrams');
		await waitForTikz();

		// The exporter keeps an index of what it already wrote and would skip every page it
		// finds unchanged, so start the second pass from an empty folder.
		const fs = require('node:fs');
		for (const entry of fs.readdirSync('/output')) {
			fs.rmSync('/output/' + entry, { recursive: true, force: true });
		}

		console.log('[export-vault] export pass 2 of 2: writes the final pages');
		await plugin.exportDocker();
		console.log('[export-vault] export finished');

		await writeMathJaxFonts();
	} catch (error) {
		console.error('[export-vault] EXPORT FAILED: ' + (error && error.stack ? error.stack : error));
	} finally {
		await sleep(4000);
		console.log('[export-vault] stopping Obsidian');
		require('node:process').kill(process.pid, 'SIGKILL');
	}
})();
