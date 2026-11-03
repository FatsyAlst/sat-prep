/* Draws the vault's charts live on the website, the way the Charts plugin draws them in
   Obsidian (same Chart.js version, same config), so they react to hovering and follow the
   light/dark switch. The export records each chart's config on its block (data-chart-config);
   the picture the exporter took stays in the page as a fallback until the live chart is drawn.

   The vault's charts were written for light mode and some set dark ink explicitly
   (rgba(0, 0, 0, a)). In dark mode that ink is turned light so labels and grid stay readable. */
(function () {
	if (window.liveCharts) return;
	window.liveCharts = true;

	var CHART_JS = "site-lib/scripts/chart.min.js";
	var drawn = []; // { block, canvas, chart }
	var loading = null;

	function loadChartJs() {
		if (window.Chart) return Promise.resolve();
		if (!loading) {
			loading = new Promise(function (resolve, reject) {
				var script = document.createElement("script");
				script.src = CHART_JS;
				script.onload = resolve;
				script.onerror = reject;
				document.head.appendChild(script);
			});
		}
		return loading;
	}

	function isDark() {
		return document.body.classList.contains("theme-dark");
	}

	var DARK_INK = /^rgba?\(\s*0\s*,\s*0\s*,\s*0\s*(?:,\s*([\d.]+)\s*)?\)$/;

	function adapt(value, theme, style, dark) {
		if (typeof value === "string") {
			if (theme.border && value.trim() === theme.border) {
				return style.getPropertyValue("--background-modifier-border").trim() || value;
			}
			var ink = dark && value.match(DARK_INK);
			if (ink) return "rgba(255, 255, 255, " + (ink[1] === undefined ? 1 : ink[1]) + ")";
			return value;
		}
		if (Array.isArray(value)) return value.map(function (v) { return adapt(v, theme, style, dark); });
		if (value && typeof value === "object") {
			var out = {};
			for (var key in value) out[key] = adapt(value[key], theme, style, dark);
			return out;
		}
		return value;
	}

	function draw(block) {
		var config, theme;
		try {
			config = JSON.parse(block.getAttribute("data-chart-config"));
			theme = JSON.parse(block.getAttribute("data-chart-theme") || "{}");
		} catch (error) {
			console.error("live chart: unreadable config", error);
			return;
		}
		var style = getComputedStyle(block);
		// What the Charts plugin sets globally before drawing.
		Chart.defaults.color = style.getPropertyValue("--text-muted").trim() || Chart.defaults.color;
		var font = style.getPropertyValue("--mermaid-font").trim();
		if (font) Chart.defaults.font.family = font;

		var entry = drawn.find(function (d) { return d.block === block; });
		if (!entry) {
			var canvas = document.createElement("canvas");
			var picture = block.querySelector(":scope > img");
			block.insertBefore(canvas, picture || block.firstChild);
			entry = { block: block, canvas: canvas, chart: null, picture: picture };
			drawn.push(entry);
		}
		if (entry.chart) entry.chart.destroy();
		try {
			entry.chart = new Chart(entry.canvas.getContext("2d"), adapt(config, theme, style, isDark()));
			if (entry.picture) entry.picture.style.display = "none";
		} catch (error) {
			console.error("live chart: could not draw", error);
			entry.canvas.remove();
			drawn.splice(drawn.indexOf(entry), 1);
		}
	}

	function drawNew() {
		var blocks = Array.prototype.filter.call(
			document.querySelectorAll("[data-chart-config]"),
			function (b) { return !drawn.some(function (d) { return d.block === b; }); }
		);
		// forget charts whose page was replaced
		drawn = drawn.filter(function (d) {
			if (document.contains(d.block)) return true;
			if (d.chart) d.chart.destroy();
			return false;
		});
		if (!blocks.length) return;
		loadChartJs().then(function () { blocks.forEach(draw); }, function () {
			console.error("live chart: Chart.js did not load, keeping the pictures");
		});
	}

	function redrawAll() {
		if (!window.Chart) return;
		drawn.forEach(function (d) { draw(d.block); });
	}

	function start() {
		drawNew();
		var lastDark = isDark();
		new MutationObserver(function () {
			drawNew();
			if (isDark() !== lastDark) {
				lastDark = isDark();
				redrawAll();
			}
		}).observe(document.body, { childList: true, subtree: true, attributes: true, attributeFilter: ["class"] });
	}

	if (document.body) start();
	else document.addEventListener("DOMContentLoaded", start);
})();
