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
from tools.asserts import assert_cart_count, assert_products_match, assert_products_sorted
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
        product_indexes_list = [0, 1, 2, 3, 4, 5]
        products_page_with_state.item_view_component.click_add_to_cart_button(indexes=product_indexes_list)
        cart_badge_count = products_page_with_state.navbar.get_cart_badge_count()
        assert_cart_count(actual_count=cart_badge_count, expected_count=len(product_indexes_list))
        selected_product = products_page_with_state.item_view_component.get_item_data(indexes=product_indexes_list)
        products_page_with_state.navbar.open_cart()
        cart_page_with_state.item_view_component.check_visible(indexes=product_indexes_list, added=True, has_image=False)
        cart_count_items = cart_page_with_state.get_cart_items_count()
        assert_cart_count(actual_count=cart_count_items, expected_count=len(product_indexes_list))
        selected_product_in_cart = cart_page_with_state.item_view_component.get_item_data()
        assert_products_match(expected_products=selected_product, actual_products=selected_product_in_cart, context="Products page to cart page")

    @allure.feature(AllureFeature.CART)
    @allure.story(AllureStories.ADD_RANDOM_PRODUCTS_TO_CART)
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.cart
    def test_add_random_products_to_cart(self, products_page_with_state: ProductsPage, cart_page_with_state: CartPage):
        products_to_add_count = random.randint(1, 6)
        product_indexes_list = random.sample(range(0, 6), products_to_add_count)
        products_page_with_state.open(AppRoute.PRODUCTS)
        products_page_with_state.item_view_component.click_add_to_cart_button(indexes=product_indexes_list)
        image_cart_count = products_page_with_state.navbar.get_cart_badge_count()
        assert_cart_count(actual_count=image_cart_count, expected_count=len(product_indexes_list))
        selected_product = products_page_with_state.item_view_component.get_item_data(indexes=product_indexes_list)
        products_page_with_state.navbar.open_cart()
        cart_page_with_state.item_view_component.check_visible(added=True, has_image=False)
        cart_count_items = cart_page_with_state.get_cart_items_count()
        assert_cart_count(actual_count=cart_count_items, expected_count=len(product_indexes_list))
        selected_product_in_cart = cart_page_with_state.item_view_component.get_item_data()
        assert_products_match(expected_products=selected_product, actual_products=selected_product_in_cart, context="Products page to cart page")

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
        assert_products_sorted(actual_items=after_sorting, option=sort_option)


