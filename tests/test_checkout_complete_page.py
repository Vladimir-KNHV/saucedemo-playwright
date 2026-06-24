from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.products_page import ProductsPage
from tools.routes import AppRoute
import pytest
import allure
from allure_commons.types import Severity

from tools.allure_tools.epics import AllureEpic
from tools.allure_tools.features import AllureFeature
from tools.allure_tools.stories import AllureStories

@pytest.mark.regression
@pytest.mark.checkout_complete
@allure.epic(AllureEpic.PURCHASE)
@allure.feature(AllureFeature.CHECKOUT_COMPLETE)
class TestCheckoutCompletePage:

    @allure.story(AllureStories.OPEN_CHECKOUT_COMPLETE_PAGE)
    @allure.severity(Severity.CRITICAL)
    def test_navigation_to_checkout_complete_page(self, checkout_overview_page_with_state: CheckoutOverviewPage, checkout_complete_page_with_state: CheckoutCompletePage):
        checkout_overview_page_with_state.open(AppRoute.CHECKOUT_OVERVIEW)
        checkout_overview_page_with_state.click_finish_button()
        checkout_complete_page_with_state.check_visible_checkout_complete_page()

    @allure.story(AllureStories.BACK_TO_PRODUCTS_FROM_CHECKOUT_COMPLETE)
    @allure.severity(Severity.NORMAL)
    def test_back_to_products_from_checkout_complete_page(self, checkout_complete_page_with_state: CheckoutCompletePage, products_page_with_state: ProductsPage):
        checkout_complete_page_with_state.open(AppRoute.CHECKOUT_COMPLETE)
        checkout_complete_page_with_state.click_back_home_button()
        products_page_with_state.check_visible_products_page()