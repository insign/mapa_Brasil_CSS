const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Handle dialogs by accepting them
  page.on('dialog', dialog => dialog.accept());

  await page.goto('http://localhost:8000/map.html');

  // Wait for the SVG map to be loaded
  await page.waitForSelector('#map-container svg');

  // Verify hover effect on a state (e.g., 'ac')
  await page.hover('#ac');
  const acState = await page.$('#ac');
  const acColor = await acState.evaluate(node => getComputedStyle(node).getPropertyValue('fill'));
  console.log(`Hover color for AC: ${acColor}`);

  // Verify click event on a state (e.g., 'sp')
  await page.click('#sp');

  // Take a screenshot
  await page.screenshot({ path: 'screenshot.png' });

  await browser.close();
})();
