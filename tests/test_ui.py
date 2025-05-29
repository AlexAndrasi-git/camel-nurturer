import pytest
from playwright.sync_api import sync_playwright
from pages.teveclubMainPage import TeveClubMainPage
from pages.teveclubTevePage import TeveclubTevePage
import tests_api
import os


@pytest.fixture
def browser_setup():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        mainPage = TeveClubMainPage(page)

        yield mainPage

        browser.close()


def test_feeding_and_teaching_teve(browser_setup):
    try:
        tests_api.test_teveclub_sanity_check()
    except AssertionError:
        pytest.skip("Skipping the UI test because the API sanity check failed")

    username = os.getenv("TEVECLUB_USERNAME")
    password = os.getenv("TEVECLUB_PASSWORD")

    browser_setup.test_login_with_valid_user(username, password)

    tevePage = TeveclubTevePage(browser_setup.page)
    tevePage.test_give_food_and_drink_to_teve()
