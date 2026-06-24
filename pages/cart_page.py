from components.item_view_component import ItemViewComponent
from elements.button import Button
from elements.container import Container
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page
import allure
from components.navigation.navbar_component import NavbarComponent
import re
from tools.routes import AppRoute

class CartPage(BasePage):
    item_view_component: ItemViewComponent

    def __init__(self, page: Page):
        super().__init__(page)

        self.item_view_component = ItemViewComponent(page)

        self.navbar = NavbarComponent(page)

        self._cart_title = Text(page, '[data-test="title"]', 'cart title')
        self._cart_qty_label = Text(page, '[data-test="cart-quantity-label"]', 'cart qty label')
        self._cart_desc_label = Text(page, '[data-test="cart-desc-label"]', 'cart desc label')

        self._cart_item = Container(page, '[data-test="inventory-item"]', 'cart item')


        self._cart_continue_shopping_button = Button(page, '[data-test="continue-shopping"]', 'continue button')
        self._cart_checkout_button = Button(page, '[data-test="checkout"]', 'checkout button')

    @allure.step('Check visible cart page')
    def check_visible_cart_page(self):
        self._cart_title.check_visible()
        self._cart_title.check_have_text('Your Cart')

        self._cart_qty_label.check_visible()
        self._cart_qty_label.check_have_text('QTY')

        self._cart_desc_label.check_visible()
        self._cart_desc_label.check_have_text('Description')
        self.check_current_url(re.compile(f'.*{AppRoute.CART.value}'))

    @allure.step('Check cart is empty')
    def check_cart_is_empty(self):
        assert self.get_cart_items_count() == 0

    def click_continue_shopping_button(self):
        self._cart_continue_shopping_button.click()

    def click_checkout_button(self):
        self._cart_checkout_button.click()

    def get_cart_items_count(self):
        return self._cart_item.count()



    