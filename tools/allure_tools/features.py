from enum import Enum

class AllureFeature(str, Enum):
    LOGIN = "Login"
    CHECKOUT = 'Checkout'
    SORTING = "Sorting"
    PRODUCT_CATALOG = "Product Catalog"
    CART = "Cart"
    ITEM_PAGE = "Item Page"
    CHECKOUT_INFO = "Checkout Information"
    CHECKOUT_OVERVIEW = "Checkout Overview"
    CHECKOUT_COMPLETE = "Checkout Complete"