import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto('https://www.google.com/maps')

    # Wait for the page to load the search bar
    await page.wait_for_selector('input#searchboxinput')

    # Type a location into the search bar
    await page.fill('input#searchboxinput', 'restaurants near me')
    await page.click('button#searchbox-searchbutton')

    # Wait for results to load
    await page.wait_for_timeout(3000)  # Adjust time according to your needs

    # Scrape data
    names = await page.query_selector_all('h3')  # Selector for names
    for name in names:
        print(await name.inner_text())  # Print each name

    # Close the browser
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == '__main__':
    asyncio.run(main())