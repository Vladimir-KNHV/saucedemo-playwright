from enum import Enum

class AppRoute(Enum):
    LOGIN = ''
    PRODUCTS = 'inventory.html'
    CART = 'cart.html'
    CHECKOUT_INFO = 'checkout-step-one.html'
    CHECKOUT_OVERVIEW = 'checkout-step-two.html'
    CHECKOUT_COMPLETE = 'checkout-complete.html'
    ITEM = 'inventory-item.html'

