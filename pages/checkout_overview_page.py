from components.item_view_component import ItemViewComponent
from components.navigation.navbar_component import NavbarComponent
from elements.button import Button
from elements.container import Container
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page
import allure
import re
from tools.routes import AppRoute

class CheckoutOverviewPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.item_view_component = ItemViewComponent(page)
        self.navbar = NavbarComponent(page)

        self._checkout_overview_title = Text(page, '[data-test="title"]', 'checkout_overview_title')
        self._cart_qty_label = Text(page, '[data-test="cart-quantity-label"]', 'qty_label')
        self._cart_desc_label = Text(page, '[data-test="cart-desc-label"]', 'desc_label')

        self._checkout_overview_item_container = Container(page, '[data-test="inventory-item"]', 'checkout_overview_item_container')

        self._summary_info_container = Container(page, '[class="summary_info"]', 'summary_info_container')
        self._payment_label = Text(page, '[data-test="payment-info-label"]', 'payment_label')
        self._payment_info_value = Text(page, '[data-test="payment-info-value"]', 'payment_info_value')
        self._shipping_info_label = Text(page, '[data-test="shipping-info-label"]', 'shipping_info_label')
        self._shipping_info_value = Text(page, '[data-test="shipping-info-value"]', 'shipping_info_value')
        self._total_info_label = Text(page, '[data-test="total-info-label"]', 'total_info_label')
        self._total_info_value = Text(page, '[data-test="subtotal-label"]', 'total_info_value')
        self._tax_label = Text(page, '[data-test="tax-label"]', 'total_info_value')
        self._summary_total_label = Text(page, '[data-test="total-label"]', 'summary_total_label')

        self._checkout_overview_cancel_button = Button(page, '[data-test="cancel"]', 'cancel_button')
        self._checkout_overview_finish_button = Button(page, '[data-test="finish"]', 'finish_button')

    @allure.step('Check visible checkout overview page')
    def check_visible_checkout_overview_page(self):
        self._checkout_overview_title.check_visible()
        self._checkout_overview_title.check_have_text('Checkout: Overview')
        self._cart_qty_label.check_visible()
        self._cart_qty_label.check_have_text('QTY')
        self._cart_desc_label.check_visible()
        self._cart_desc_label.check_have_text('Description')
        self._summary_info_container.check_visible()

        self._payment_label.check_visible()
        self._payment_label.check_have_text('Payment Information:')

        self._payment_info_value.check_visible()
        self._payment_info_value.check_have_contain_text('SauceCard #')

        self._shipping_info_label.check_visible()
        self._shipping_info_label.check_have_text('Shipping Information:')

        self._shipping_info_value.check_visible()
        self._shipping_info_value.check_have_text('Free Pony Express Delivery!')

        self._total_info_label.check_visible()
        self._total_info_label.check_have_text('Price Total')

        self._total_info_value.check_visible()
        self._total_info_value.check_have_contain_text('Item total: $')

        self._tax_label.check_visible()
        self._tax_label.check_have_contain_text('Tax: $')

        self._summary_total_label.check_visible()
        self._summary_total_label.check_have_contain_text('Total: $')

        self.check_current_url(re.compile(f'.*{AppRoute.CHECKOUT_OVERVIEW.value}'))

    @allure.step('Check visible empty checkout overview page')
    def check_visible_empty_checkout_overview_page(self):
        self._checkout_overview_title.check_visible()
        self._checkout_overview_title.check_have_text('Checkout: Overview')
        self._cart_qty_label.check_visible()
        self._cart_qty_label.check_have_text('QTY')
        self._cart_desc_label.check_visible()
        self._cart_desc_label.check_have_text('Description')
        self._summary_info_container.check_visible()

        self._payment_label.check_visible()
        self._payment_label.check_have_text('Payment Information:')

        self._payment_info_value.check_visible()
        self._payment_info_value.check_have_contain_text('SauceCard #')

        self._shipping_info_label.check_visible()
        self._shipping_info_label.check_have_text('Shipping Information:')

        self._shipping_info_value.check_visible()
        self._shipping_info_value.check_have_text('Free Pony Express Delivery!')

        self._total_info_label.check_visible()
        self._total_info_label.check_have_text('Price Total')

        self._total_info_value.check_visible()
        self._total_info_value.check_have_text('Item total: $0')

        self._tax_label.check_visible()
        self._tax_label.check_have_text('Tax: $0.00')

        self._summary_total_label.check_visible()
        self._summary_total_label.check_have_text('Total: $0.00')
        assert self._checkout_overview_item_container.count() == 0, 'Checkout overview not empty'
        self.check_current_url(re.compile(f'.*{AppRoute.CHECKOUT_OVERVIEW.value}'))

    @allure.step('Get summary total price')
    def get_summary_total_price(self) -> float:
        return float(self._total_info_value.get_text().replace('Item total: $', ''))

    def click_cancel_button(self):
        self._checkout_overview_cancel_button.click()

    def click_finish_button(self):
        self._checkout_overview_finish_button.click()
        

