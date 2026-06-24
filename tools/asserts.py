import allure
from enums.sort_option import SortOption
from tools.allure_tools.allure_formatters import format_items, format_sorting


def assert_sorted_products(after: list, option: SortOption):
    if option in (SortOption.NAME_AZ, SortOption.PRICE_LOW_HIGH):
        expected = sorted(after)
    elif option in (SortOption.NAME_ZA, SortOption.PRICE_HIGH_LOW):
        expected = sorted(after, reverse=True)
    else:
        raise ValueError(f"Unknown sort option: {option}")

    step = f'Assert products sorted by value {option.name}'
    with allure.step(step):
        allure.attach(format_sorting(after), name="Actual sorting result", attachment_type=allure.attachment_type.TEXT)
        assert expected == after

def assert_product_consistency(expected: list, actual: list, context: str):
    step = f"Assert product consistency {context}"
    with allure.step(step):
        allure.attach(format_items(expected), name="expected", attachment_type=allure.attachment_type.TEXT)
        allure.attach(format_items(actual), name="actual", attachment_type=allure.attachment_type.TEXT)

        assert expected == actual

def assert_prices_match(expected: float, actual: float):
    step = f"Assert item prices {expected} match total price {actual}"
    with allure.step(step):
        assert expected == actual

def assert_cart_count(cart_count: int, total: int):
    step = f"Assert cart count {cart_count} match total count {total}"
    with allure.step(step):
        assert cart_count == total


def assert_remove(before: list, removed_items: list, items: list):
    step = f"Assert removed item not in items"
    with allure.step(step):
        allure.attach(format_items(before), name="Before removing", attachment_type=allure.attachment_type.TEXT)
        allure.attach(format_items(removed_items), name="Removed_items", attachment_type=allure.attachment_type.TEXT)
        allure.attach(format_items(items), name="Items after remove", attachment_type=allure.attachment_type.TEXT)

        for item in removed_items:
            assert item not in items
