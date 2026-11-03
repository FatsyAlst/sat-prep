// Injected into the headless Obsidian window (see publish-website.yml).
//
// Same job as the exporter's own docker/export-vault.mjs: enable the vault's plugins,
// enable "Webpage HTML Export" and export every note to /output. The difference is that
// a failure is printed with its stack trace, and Obsidian is given a moment to flush its
// console to the log before the process is stopped, so a broken export explains itself.

console.log('[export-vault] starting');

(async () => {
	const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
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
	} catch (error) {
		console.error('[export-vault] EXPORT FAILED: ' + (error && error.stack ? error.stack : error));
	} finally {
		await sleep(4000);
		console.log('[export-vault] stopping Obsidian');
		require('node:process').kill(process.pid, 'SIGKILL');
	}
})();
