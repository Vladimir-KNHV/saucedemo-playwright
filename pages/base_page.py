from playwright.sync_api import Page, expect
from typing import Pattern
import allure
from tools.routes import AppRoute
from config import settings

class BasePage:
    def __init__(self, page: Page):
        self._page = page

    def open(self, route: AppRoute):
        with allure.step(f'Opening url "{str(settings.app_url)}{route.value}"'):
            self._page.goto(f"{str(settings.app_url)}{route.value}")

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking current url matches pattern "{expected_url.pattern}"'):
            expect(self._page).to_have_url(expected_url)

    def check_url_not_contain_pattern(self, pattern: Pattern[str]):
        with allure.step(f'Checking URL does not match pattern "{pattern.pattern}"'):
            expect(self._page).not_to_have_url(pattern)



    