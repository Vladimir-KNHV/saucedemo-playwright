from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
import allure
import pytest
from tools.routes import AppRoute
from test_data.data_fixtures.checkout_fixture import invalid_checkout_case
from test_data.models.checkout import CheckoutNegativeCase
import re
from tools.allure_tools.epics import AllureEpic
from tools.allure_tools.stories import AllureStories
from tools.allure_tools.features import AllureFeature
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.checkout
@allure.epic(AllureEpic.PURCHASE)
class TestCheckoutInfoPage:

    @allure.feature(AllureFeature.CHECKOUT_INFO)
    @allure.story(AllureStories.OPEN_CHECKOUT_INFO_PAGE)
    @allure.severity(Severity.CRITICAL)
    def test_navigation_to_checkout_info_page(self, cart_page_with_state: CartPage, checkout_info_page_with_state: CheckoutInfoPage):
        cart_page_with_state.open(AppRoute.CART)
        cart_page_with_state.click_checkout_button()
        checkout_info_page_with_state.check_visible_checkout_info_page()

    @allure.feature(AllureFeature.CHECKOUT_INFO)
    @allure.story(AllureStories.INVALID_CHECKOUT_INFO)
    @allure.severity(Severity.CRITICAL)
    def test_invalid_fill_checkout_info_form(self, checkout_info_page_with_state: CheckoutInfoPage, invalid_checkout_case: CheckoutNegativeCase):
        case = invalid_checkout_case
        checkout_info_page_with_state.open(AppRoute.CHECKOUT_INFO)
        checkout_info_page_with_state.fill_checkout_info_form(first_name=case.first_name, last_name=case.last_name, zip_code=case.postal_code)
        checkout_info_page_with_state.click_checkout_continue_button()
        checkout_info_page_with_state.check_checkout_error_alert(epic_sadface=case.epic_sadface)
        checkout_info_page_with_state.check_current_url(re.compile(f'.*{AppRoute.CHECKOUT_INFO.value}'))

    @allure.feature(AllureFeature.CHECKOUT_INFO)
    @allure.story(AllureStories.SUCCESSFUL_CHECKOUT_INFO)
    @allure.severity(Severity.CRITICAL)
    def test_successful_fill_checkout_info_form(self, checkout_info_page_with_state: CheckoutInfoPage, checkout_overview_page_with_state: CheckoutOverviewPage):

        checkout_info_page_with_state.open(AppRoute.CHECKOUT_INFO)
        checkout_info_page_with_state.fill_checkout_info_form(first_name='user', last_name='user', zip_code='123345')
        checkout_info_page_with_state.click_checkout_continue_button()
        checkout_overview_page_with_state.check_visible_checkout_overview_page()

    @allure.feature(AllureFeature.CHECKOUT_INFO)
    @allure.story(AllureStories.BACK_TO_CART_FROM_CHECKOUT_INFO)
    @allure.severity(Severity.NORMAL)
    def test_back_to_cart_from_checkout_info_page(self, checkout_info_page_with_state: CheckoutInfoPage, cart_page_with_state: CartPage):
        checkout_info_page_with_state.open(AppRoute.CHECKOUT_INFO)
        checkout_info_page_with_state.check_visible_checkout_info_page()
        checkout_info_page_with_state.click_checkout_cancel_button()
        cart_page_with_state.check_visible_cart_page()

