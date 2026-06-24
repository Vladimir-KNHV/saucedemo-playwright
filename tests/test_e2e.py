
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.item_page import ItemPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config import settings
import allure
import pytest
from allure_commons.types import Severity
from tools.allure_tools.epics import AllureEpic
from tools.allure_tools.features import AllureFeature
from tools.allure_tools.stories import AllureStories
from tools.routes import AppRoute
from tools.asserts import assert_product_consistency, assert_prices_match


@pytest.mark.regression
@pytest.mark.e2e
@allure.epic(AllureEpic.PURCHASE)
@allure.feature(AllureFeature.CHECKOUT)
class TestE2E:
    
    @allure.story(AllureStories.SUCCESSFUL_PURCHASE)
    @allure.severity(Severity.BLOCKER)
    def test_e2e(
            self,
            login_page: LoginPage,
            products_page: ProductsPage,
            item_page: ItemPage,
            cart_page: CartPage,
            checkout_info_page: CheckoutInfoPage,
            checkout_overview_page: CheckoutOverviewPage,
            checkout_complete_page: CheckoutCompletePage,
    ):
        login_page.open(AppRoute.LOGIN)

        login_page.fill_login_form(username=settings.test_user.username, password=settings.test_user.password)
        login_page.click_login_button()

        products_page.check_visible_products_page()
        products_page.item_view_component.click_add_to_cart_button(indexes=0)
        products_page.item_view_component.check_visible(indexes=0, added=True)

        expected = products_page.item_view_component.get_item_data(indexes=0)
        products_page.navbar.open_cart()
        cart_page.check_visible_cart_page()

        cart_page.item_view_component.check_visible(added=True, has_image=False)

        actual_in_cart = cart_page.item_view_component.get_item_data()

        assert_product_consistency(expected=expected, actual=actual_in_cart, context="Product to cart")

        cart_page.click_checkout_button()

        checkout_info_page.check_visible_checkout_info_page()

        checkout_info_page.fill_checkout_info_form(
            first_name='sdgdg',
            last_name='dgadg',
            zip_code='5246'
        )
        checkout_info_page.click_checkout_continue_button()

        checkout_overview_page.check_visible_checkout_overview_page()

        checkout_overview_page.item_view_component.check_visible(has_image=False, has_button=False)
        actual_in_overview = checkout_overview_page.item_view_component.get_item_data()


        assert_product_consistency(expected=actual_in_cart, actual=actual_in_overview, context="Cart to checkout")
        price = float(sum(checkout_overview_page.item_view_component.get_all_prices()))
        total_price = checkout_overview_page.get_summary_total_price()

        assert_prices_match(expected=price, actual=total_price)

        checkout_overview_page.click_finish_button()

        checkout_complete_page.check_visible_checkout_complete_page()


    



