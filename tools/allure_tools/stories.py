from enum import Enum

class AllureStories(str, Enum):
    SUCCESSFUL_LOGIN = 'Successful login'
    INVALID_LOGIN = 'Invalid login'
    SUCCESSFUL_PURCHASE = 'Successful purchase'
    SORT_PRODUCTS = "Sort products"
    OPEN_PRODUCTS_PAGE = "Open products page"
    ADD_ALL_PRODUCT_TO_CART = "Add all products to cart"
    ADD_RANDOM_PRODUCTS_TO_CART = "Add random products to cart"

    OPEN_CART_PAGE = "Open cart page"
    REMOVE_ALL_PRODUCTS_FROM_CART = "Remove all products from cart"
    REMOVE_RANDOM_PRODUCTS_FROM_CART = "Remove random products from cart"

    OPEN_ITEM_PAGE = "Open item page"
    ADD_PRODUCT_TO_CART_FROM_ITEM_PAGE = "Add product to cart from item page"
    REMOVE_PRODUCT_FROM_ITEM_PAGE = "Remove product from item page"
    BACK_TO_PRODUCTS_FROM_ITEM_PAGE = "Back to products from item page"
    BACK_TO_PRODUCTS_FROM_CART_PAGE = "Back to products from cart page"

    OPEN_CHECKOUT_INFO_PAGE = "Open checkout information page"
    INVALID_CHECKOUT_INFO = "Invalid checkout information"
    SUCCESSFUL_CHECKOUT_INFO = "Successful checkout information"
    BACK_TO_CART_FROM_CHECKOUT_INFO = "Back to cart from checkout information page"
    OPEN_CHECKOUT_OVERVIEW_PAGE = "Open checkout overview page"
    CANCEL_CHECKOUT_OVERVIEW = "Cancel checkout overview"
    VERIFY_PRODUCTS_ON_CHECKOUT_OVERVIEW = "Verify products on checkout overview"
    VERIFY_TOTAL_PRICE = "Verify total price"
    OPEN_CHECKOUT_COMPLETE_PAGE = "Open checkout complete page"
    BACK_TO_PRODUCTS_FROM_CHECKOUT_COMPLETE = "Back to products from checkout complete page"