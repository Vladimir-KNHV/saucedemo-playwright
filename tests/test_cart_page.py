from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from tools.routes import AppRoute
import random
from tools.asserts import *
import allure
import pytest
from tools.allure_tools.epics import AllureEpic
from tools.allure_tools.features import AllureFeature
from tools.allure_tools.stories import AllureStories
from allure_commons.types import Severity

@pytest.mark.regression
@pytest.mark.cart
@allure.epic(AllureEpic.CART)
class TestCartPage:

    @allure.feature(AllureFeature.CART)
    @allure.story(AllureStories.OPEN_CART_PAGE)
    @allure.severity(Severity.CRITICAL)
    def test_navigation_to_cart_page(self, products_page_with_state: ProductsPage, cart_page_with_state: CartPage):
        products_page_with_state.open(AppRoute.PRODUCTS)
        products_page_with_state.navbar.open_cart()
        cart_page_with_state.check_visible_cart_page()
        cart_page_with_state.check_cart_is_empty()

    @allure.feature(AllureFeature.CART)
    @allure.story(AllureStories.BACK_TO_PRODUCTS_FROM_CART_PAGE)
    @allure.severity(Severity.CRITICAL)
    def test_navigation_back_to_products_page_from_cart_page(self, products_page_with_state: ProductsPage, cart_page_with_state: CartPage):
        products_page_with_state.open(AppRoute.PRODUCTS)
        products_page_with_state.navbar.open_cart()
        cart_page_with_state.check_visible_cart_page()
        cart_page_with_state.click_continue_shopping_button()
        products_page_with_state.check_visible_products_page()

    @allure.feature(AllureFeature.CART)
    @allure.story(AllureStories.REMOVE_ALL_PRODUCTS_FROM_CART)
    @allure.severity(Severity.CRITICAL)
    def test_remove_all_products_from_cart(self, products_page_with_state: ProductsPage, cart_page_with_state: CartPage):
        products_page_with_state.open(AppRoute.PRODUCTS)
        num = [0,1,2,3,4,5]
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

        removed_names = [items.name for items in selected_product_in_cart]

        cart_page_with_state.item_view_component.click_remove_by_name(removed_names)
        after_removing = cart_page_with_state.get_cart_items_count()
        assert_cart_count(cart_count=after_removing, total=0)

    @allure.feature(AllureFeature.CART)
    @allure.story(AllureStories.REMOVE_RANDOM_PRODUCTS_FROM_CART)
    @allure.severity(Severity.CRITICAL)
    def test_remove_random_products_from_cart(self, products_page_with_state: ProductsPage, cart_page_with_state: CartPage):
        length = random.randint(1, 6)
        result = random.sample(range(0, 6), length)
        products_page_with_state.open(AppRoute.PRODUCTS)
        products_page_with_state.item_view_component.click_add_to_cart_button(indexes=result)
        icon_cart_count = products_page_with_state.navbar.get_count_in_icon_cart()
        assert_cart_count(cart_count=icon_cart_count, total=len(result))
        selected_product = products_page_with_state.item_view_component.get_item_data(indexes=result)
        products_page_with_state.navbar.open_cart()
        cart_page_with_state.item_view_component.check_visible(added=True, has_image=False)
        cart_count_items = cart_page_with_state.get_cart_items_count()
        assert_cart_count(cart_count=cart_count_items, total=len(result))
        selected_product_in_cart = cart_page_with_state.item_view_component.get_item_data()
        assert_product_consistency(expected=selected_product, actual=selected_product_in_cart, context="Products page to cart page")


        remove_index = random.sample(range(0, len(result)), random.randint(1, len(result)))
        removed_item = cart_page_with_state.item_view_component.get_item_data(indexes=remove_index)
        removed_names = [item.name for item in removed_item]
        cart_page_with_state.item_view_component.click_remove_by_name(removed_names)

        items_in_cart = cart_page_with_state.item_view_component.get_item_data()
        assert_remove(before=selected_product_in_cart, removed_items=removed_item, items=items_in_cart)
