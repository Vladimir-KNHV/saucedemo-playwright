from playwright.sync_api import Page, expect
from typing import Pattern
import allure
class BaseComponent:
    def __init__(self, page: Page):
        self._page = page

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking current url matches pattern "{expected_url.pattern}"'):
            expect(self._page).to_have_url(expected_url)