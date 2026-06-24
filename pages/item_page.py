from components.item_view_component import ItemViewComponent
from components.navigation.navbar_component import NavbarComponent
from elements.button import Button
from pages.base_page import BasePage
from playwright.sync_api import Page
import re
from tools.routes import AppRoute

class ItemPage(BasePage):
    item_view_component: ItemViewComponent
    def __init__(self,page: Page):
        super().__init__(page)

        self.item_view_component = ItemViewComponent(page)
        self.navbar = NavbarComponent(page)

        self._back_to_products_button = Button(page, '[data-test="back-to-products"]', 'back to products button')

    def check_visible_item_page(self):
        self.item_view_component.check_visible()
        self._back_to_products_button.check_have_text('Back to products')
        self.check_current_url(re.compile(f'.*{AppRoute.ITEM.value}'))


    def click_back_to_products_button(self):
        self._back_to_products_button.click()

