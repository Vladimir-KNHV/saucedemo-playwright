from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from tools.routes import AppRoute
from tools.asserts import *
import pytest
import allure
from tools.allure_tools.epics import AllureEpic
from tools.allure_tools.features import AllureFeature
from tools.allure_tools.stories import AllureStories
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.checkout
@allure.epic(AllureEpic.PURCHASE)
@allure.feature(AllureFeature.CHECKOUT_OVERVIEW)
class TestCheckoutOverviewPage:


    @allure.story(AllureStories.OPEN_CHECKOUT_OVERVIEW_PAGE)
    @allure.severity(Severity.CRITICAL)
    def test_navigation_to_checkout_overview_page(self, checkout_info_page_with_state: CheckoutInfoPage, checkout_overview_page_with_state: CheckoutOverviewPage):
        checkout_info_page_with_state.open(AppRoute.CHECKOUT_INFO)
        checkout_info_page_with_state.fill_checkout_info_form(first_name='user', last_name='user', zip_code='123345')
        checkout_info_page_with_state.click_checkout_continue_button()
        checkout_overview_page_with_state.check_visible_empty_checkout_overview_page()

    @allure.story(AllureStories.CANCEL_CHECKOUT_OVERVIEW)
    @allure.severity(Severity.NORMAL)
    def test_back_to_products_from_checkout_overview_page(self, checkout_overview_page_with_state: CheckoutOverviewPage, products_page_with_state: ProductsPage):
        checkout_overview_page_with_state.open(AppRoute.CHECKOUT_OVERVIEW)
        checkout_overview_page_with_state.check_visible_checkout_overview_page()
        checkout_overview_page_with_state.click_cancel_button()
        products_page_with_state.check_visible_products_page()

    @allure.story(AllureStories.VERIFY_PRODUCTS_ON_CHECKOUT_OVERVIEW)
    @allure.severity(Severity.CRITICAL)
    def test_added_products_is_displayed_on_checkout_page(self, products_page_with_state: ProductsPage, cart_page_with_state: CartPage, checkout_info_page_with_state: CheckoutInfoPage, checkout_overview_page_with_state: CheckoutOverviewPage):
        products_page_with_state.open(AppRoute.PRODUCTS)
        products_page_with_state.item_view_component.click_add_to_cart_button(indexes=[0,1,2,3,4,5])
        expected = products_page_with_state.item_view_component.get_item_data()
        products_page_with_state.navbar.open_cart()
        cart_page_with_state.click_checkout_button()
        checkout_info_page_with_state.fill_checkout_info_form(first_name='user', last_name='user', zip_code='123345')
        checkout_info_page_with_state.click_checkout_continue_button()
        actual = checkout_overview_page_with_state.item_view_component.get_item_data()
        assert_products_match(expected_products=expected, actual_products=actual, context='Products to checkout overview')
        checkout_overview_page_with_state.item_view_component.check_visible(has_image=False, has_button=False)

    @allure.story(AllureStories.VERIFY_TOTAL_PRICE)
    @allure.severity(Severity.CRITICAL)
    def test_checkout_overview_displays_correct_products_total_price(self, products_page_with_state: ProductsPage, cart_page_with_state: CartPage, checkout_info_page_with_state: CheckoutInfoPage, checkout_overview_page_with_state: CheckoutOverviewPage):
        products_page_with_state.open(AppRoute.PRODUCTS)
        products_page_with_state.item_view_component.click_add_to_cart_button(indexes=[0,1,2,3,4,5])
        expected = sum(products_page_with_state.item_view_component.get_all_prices())
        products_page_with_state.navbar.open_cart()
        cart_page_with_state.click_checkout_button()
        checkout_info_page_with_state.fill_checkout_info_form(first_name='user', last_name='user', zip_code='123345')
        checkout_info_page_with_state.click_checkout_continue_button()
        actual = checkout_overview_page_with_state.get_summary_total_price()
        assert_total_price_matches(expected=expected, actual=actual)





