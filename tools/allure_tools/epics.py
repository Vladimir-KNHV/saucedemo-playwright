from enum import Enum

class  AllureEpic(str, Enum):
    AUTHORIZATION = "Authorization"
    PURCHASE = 'Purchase'
    PRODUCTS = "Products"
    CART = "Cart"
    ITEM = "Item"