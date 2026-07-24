
from pages.products_page import ProductsPage
from pages.item_page import ItemPage
from pages.cart_page import CartPage
from tools.routes import AppRoute
from tools.asserts import *
import pytest
import allure
from allure_commons.types import Severity
from tools.allure_tools.epics import AllureEpic
from tools.allure_tools.features import AllureFeature
from tools.allure_tools.stories import AllureStories

@pytest.mark.regression
@pytest.mark.item
@allure.epic(AllureEpic.PRODUCTS)
class TestItemPage:

    @allure.feature(AllureFeature.ITEM_PAGE)
    @allure.story(AllureStories.OPEN_ITEM_PAGE)
    @allure.severity(Severity.CRITICAL)
    def test_navigation_to_item_page(self, products_page_with_state: ProductsPage, item_page_with_state: ItemPage):
        products_page_with_state.open(AppRoute.PRODUCTS)
        expected_item = products_page_with_state.item_view_component.get_item_data(indexes=0)
        products_page_with_state.item_view_component.open_item_page(index=0)
        item_page_with_state.check_visible_item_page()
        actual_item = item_page_with_state.item_view_component.get_item_data()
        assert_products_match(expected_products=expected_item, actual_products=actual_item, context='Products page to item page')

    @allure.feature(AllureFeature.ITEM_PAGE)
    @allure.story(AllureStories.BACK_TO_PRODUCTS_FROM_ITEM_PAGE)
    @allure.severity(Severity.CRITICAL)
    def test_navigation_back_to_products_page(self, products_page_with_state: ProductsPage, item_page_with_state: ItemPage):
        products_page_with_state.open(AppRoute.PRODUCTS)
        products_page_with_state.item_view_component.open_item_page(index=0)
        item_page_with_state.check_visible_item_page()
        item_page_with_state.click_back_to_products_button()
        products_page_with_state.check_visible_products_page()

    @allure.feature(AllureFeature.ITEM_PAGE)
    @allure.story(AllureStories.ADD_PRODUCT_TO_CART_FROM_ITEM_PAGE)
    @allure.severity(Severity.CRITICAL)
    def test_add_item_to_cart(self, products_page_with_state: ProductsPage, item_page_with_state: ItemPage, cart_page_with_state: CartPage):
        products_page_with_state.open(AppRoute.PRODUCTS)
        expected_item = products_page_with_state.item_view_component.get_item_data(indexes=0)
        products_page_with_state.item_view_component.open_item_page(index=0)
        item_page_with_state.item_view_component.click_add_to_cart_button(indexes=0)
        item_page_with_state.item_view_component.check_visible(added=True)
        count_in_icon_cart = item_page_with_state.navbar.get_cart_badge_count()
        assert_cart_count(actual_count=count_in_icon_cart, expected_count=1)
        item_page_with_state.navbar.open_cart()
        cart_page_with_state.item_view_component.check_visible(added=True, has_image=False)
        actual_item = cart_page_with_state.item_view_component.get_item_data()
        assert_products_match(expected_products=expected_item, actual_products=actual_item, context='Item page to cart page')

    @allure.feature(AllureFeature.ITEM_PAGE)
    @allure.story(AllureStories.REMOVE_PRODUCT_FROM_ITEM_PAGE)
    @allure.severity(Severity.CRITICAL)
    def test_remove_item_after_adding_to_cart(self, products_page_with_state: ProductsPage, item_page_with_state: ItemPage,cart_page_with_state: CartPage):
        products_page_with_state.open(AppRoute.PRODUCTS)
        products_page_with_state.item_view_component.open_item_page(index=0)
        item_page_with_state.item_view_component.click_add_to_cart_button(indexes=0)
        item_page_with_state.item_view_component.check_visible(added=True)
        item_page_with_state.item_view_component.click_remove_button(indexes=0)
        item_page_with_state.item_view_component.check_visible(added=False)
        item_page_with_state.navbar.open_cart()
        cart_items_count = cart_page_with_state.get_cart_items_count()
        assert_cart_count(actual_count=cart_items_count, expected_count=0)


