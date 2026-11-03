// Injected into the headless Obsidian window (see publish-website.yml).
//
// Same job as the exporter's own docker/export-vault.mjs: enable the vault's plugins,
// enable "Webpage HTML Export" and export every note to /output. Differences:
//   - a failure is printed with its stack trace, and Obsidian is given a moment to flush its
//     console to the log before it is stopped, so a broken export explains itself;
//   - the MathJax fonts are written to the site. The exporter points the formulas' CSS at
//     site-lib/fonts/mathjax_*.woff but never saves those files, so without this step the
//     formulas fall back to a plain serif font.

console.log('[export-vault] starting');

(async () => {
	const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

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
				const name = decodeURIComponent(url.split('?')[0].split('/').pop());
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

		console.log('[export-vault] enabling Webpage HTML Export');
		await this.app.plugins.enablePlugin('webpage-html-export');
		const plugin = await this.app.plugins.getPlugin('webpage-html-export');
		if (!plugin) throw new Error('Webpage HTML Export did not load');

		console.log('[export-vault] exporting to /output');
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
