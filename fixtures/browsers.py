import pytest
from playwright.sync_api import Page, Playwright
from typing import Generator
from _pytest.fixtures import SubRequest
from tools.playwright.page import initialize_page
from config import settings

@pytest.fixture(params=settings.browsers)
def page(request: SubRequest, playwright: Playwright) -> Generator[Page, None, None]:
    yield from initialize_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param
    )



@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    page.goto('https://www.saucedemo.com/')
    page.locator('[data-test="username"]').fill(settings.test_user.username)
    page.locator('[data-test="password"]').fill(settings.test_user.password)
    page.locator('[data-test="login-button"]').click()
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    context.storage_state(path=settings.browser_state_file)

    context.close()
    browser.close()




@pytest.fixture(params=settings.browsers)
def page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Generator[Page, None, None]:
    yield from initialize_page(
        playwright,
        test_name=request.node.name,
        storage_state=settings.browser_state_file,
        browser_type=request.param
    )

