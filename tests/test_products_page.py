from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from tools.routes import AppRoute
from config import settings
import pytest
import allure
from tools.allure_tools.epics import AllureEpic
from tools.allure_tools.stories import AllureStories
from tools.allure_tools.features import AllureFeature
from allure_commons.types import Severity
import random
from tools.asserts import assert_cart_count, assert_product_consistency, assert_sorted_products
from enums.sort_option import SortOption
from pages.cart_page import CartPage

@pytest.mark.regression
@pytest.mark.products
@allure.epic(AllureEpic.PRODUCTS)
class TestProductsPage:

    @allure.feature(AllureFeature.PRODUCT_CATALOG)
    @allure.story(AllureStories.OPEN_PRODUCTS_PAGE)
    @allure.severity(Severity.CRITICAL)
    def test_navigation_to_products_page(self, login_page: LoginPage, products_page: ProductsPage):
        login_page.open(AppRoute.LOGIN)
        login_page.fill_login_form(username=settings.test_user.username, password=settings.test_user.password)
        login_page.click_login_button()
        products_page.check_visible_products_page()

    @allure.feature(AllureFeature.CART)
    @allure.story(AllureStories.ADD_ALL_PRODUCT_TO_CART)
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.cart
    def test_add_all_product_to_cart(self, products_page_with_state: ProductsPage, cart_page_with_state: CartPage):
        products_page_with_state.open(AppRoute.PRODUCTS)
        num = [0, 1, 2, 3, 4, 5]
        products_page_with_state.item_view_component.click_add_to_cart_button(indexes=num)
        image_cart_count = products_page_with_state.navbar.get_count_in_icon_cart()
        assert_cart_count(cart_count=image_cart_count, total=6)
        selected_product = products_page_with_state.item_view_component.get_item_data(indexes=num)
        products_page_with_state.navbar.open_cart()
        cart_page_with_state.item_view_component.check_visible(indexes=num, added=True, has_image=False)
        cart_count_items = cart_page_with_state.get_cart_items_count()
        assert_cart_count(cart_count=cart_count_items, total=6)
        selected_product_in_cart = cart_page_with_state.item_view_component.get_item_data()
        assert_product_consistency(expected=selected_product, actual=selected_product_in_cart, context="Products page to cart page")

    @allure.feature(AllureFeature.CART)
    @allure.story(AllureStories.ADD_RANDOM_PRODUCTS_TO_CART)
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.cart
    def test_add_random_products_to_cart(self, products_page_with_state: ProductsPage, cart_page_with_state: CartPage):
        length = random.randint(1, 6)
        result = random.sample(range(0, 5), length)
        products_page_with_state.open(AppRoute.PRODUCTS)
        products_page_with_state.item_view_component.click_add_to_cart_button(indexes=result)
        image_cart_count = products_page_with_state.navbar.get_count_in_icon_cart()
        assert_cart_count(cart_count=image_cart_count, total=len(result))
        selected_product = products_page_with_state.item_view_component.get_item_data(indexes=result)
        products_page_with_state.navbar.open_cart()
        cart_page_with_state.item_view_component.check_visible(added=True, has_image=False)
        cart_count_items = cart_page_with_state.get_cart_items_count()
        assert_cart_count(cart_count=cart_count_items, total=len(result))
        selected_product_in_cart = cart_page_with_state.item_view_component.get_item_data()
        assert_product_consistency(expected=selected_product, actual=selected_product_in_cart, context="Products page to cart page")

    @allure.feature(AllureFeature.SORTING)
    @allure.story(AllureStories.SORT_PRODUCTS)
    @allure.severity(Severity.NORMAL)
    @pytest.mark.sorting
    @pytest.mark.parametrize(
        'sort_option',
        [
            SortOption.NAME_ZA,
            SortOption.PRICE_LOW_HIGH,
            SortOption.PRICE_HIGH_LOW,
            SortOption.NAME_AZ
        ],
        ids=lambda x: x.name
    )
    def test_sort_products(self, products_page_with_state: ProductsPage, sort_option: SortOption):
        allure.dynamic.title(f"Sort products by: {sort_option.name}")
        products_page_with_state.open(AppRoute.PRODUCTS)
        products_page_with_state.sort_products(sort_option)
        after_sorting = products_page_with_state.get_sorted_products(sort_option)
        assert_sorted_products(after=after_sorting, option=sort_option)


