import pytest
from playwright.sync_api import sync_playwright

SAUCEDEMO_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def test_login_saucedemo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(SAUCEDEMO_URL)
        page.fill('input[data-test="username"]', USERNAME)
        page.fill('input[data-test="password"]', PASSWORD)
        page.click('input[data-test="login-button"]')
        # Assert successful login by checking for inventory page
        assert page.url == "https://www.saucedemo.com/inventory.html"
        browser.close()

