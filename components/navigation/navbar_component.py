from components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.button import Button
from elements.link import Link
from elements.text import Text
import allure

class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self._open_menu_button = Button(page, '[data-test="open-menu"]', 'open menu')
        self._app_title = Text(page, '[class="app_logo"]', 'app_logo')
        self._cart_link = Link(page, '[data-test="shopping-cart-link"]', 'cart icon link')
        self._logout_link = Link(page, '//*[@data-test="logout-sidebar-link"]', 'logout link')

    @allure.step('Check visible navbar')
    def check_visible(self):
        self._app_title.check_visible()
        self._app_title.check_have_text('Swag Labs')

        self._open_menu_button.check_visible()
        self._cart_link.check_visible()

    
    def open_cart(self):
        self._cart_link.click()

    def get_count_in_icon_cart(self) -> int:
        return int(self._cart_link.get_text())

    def open_menu(self):
        self._open_menu_button.click()

    def logout(self):
        self._logout_link.click()






