from playwright.sync_api import sync_playwright, Page, expect
from pathlib import Path

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the local file
        page.goto("http://localhost:8000/map.html")

        # Wait for the SVG to be loaded into the container and visible
        svg_element = page.locator("#map-container svg")
        expect(svg_element).to_be_visible()

        # Wait for a specific state to be visible to ensure rendering is complete
        state_ac = page.locator("#ac")
        expect(state_ac).to_be_visible()

        # Take a screenshot
        page.screenshot(path="jules-scratch/verification/verification.png")

        browser.close()

if __name__ == "__main__":
    run()
