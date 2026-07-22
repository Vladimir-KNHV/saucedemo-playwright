from enum import Enum

class AppRoute(Enum):
    """
    Маршруты приложения.

    Наследование только от Enum, а не от str, используется намеренно.

    Это предотвращает появление методов str (split, replace, upper и т.д.)
    в автодополнении IDE при работе с AppRoute, оставляя только элементы Enum.
    Для получения строкового значения используется `.value`.
    """
    LOGIN = ''
    PRODUCTS = 'inventory.html'
    CART = 'cart.html'
    CHECKOUT_INFO = 'checkout-step-one.html'
    CHECKOUT_OVERVIEW = 'checkout-step-two.html'
    CHECKOUT_COMPLETE = 'checkout-complete.html'
    ITEM = 'inventory-item.html'

