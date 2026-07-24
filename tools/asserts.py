import allure
from enums.sort_option import SortOption
from tools.allure_tools.allure_formatters import format_items, format_sort_result


def assert_products_sorted(actual_items: list, option: SortOption):
    if option in (SortOption.NAME_AZ, SortOption.PRICE_LOW_HIGH):
        expected = sorted(actual_items)
    elif option in (SortOption.NAME_ZA, SortOption.PRICE_HIGH_LOW):
        expected = sorted(actual_items, reverse=True)
    else:
        raise ValueError(f"Unknown sort option: {option}")

    step = f'Assert products sorted by value {option.name}'
    with allure.step(step):
        allure.attach(format_sort_result(actual_items), name="Actual sorting result", attachment_type=allure.attachment_type.TEXT)
        assert expected == actual_items

def assert_products_match(expected_products: list, actual_products: list, context: str):
    step = f"Assert product consistency: {context}"
    with allure.step(step):
        allure.attach(format_items(expected_products), name="expected", attachment_type=allure.attachment_type.TEXT)
        allure.attach(format_items(actual_products), name="actual", attachment_type=allure.attachment_type.TEXT)

        assert expected_products == actual_products

def assert_total_price_matches(expected: float, actual: float):
    step =  f"Verify total price: expected={expected}, actual={actual}"
    with allure.step(step):
        assert round(expected, 2) == round(actual, 2)

def assert_cart_count(actual_count: int, expected_count: int):
    step = (
        f"Verify cart count. "
        f"Expected: {expected_count}, Actual: {actual_count}"
    )
    with allure.step(step):
        assert actual_count == expected_count


def assert_items_removed(before_items: list, removed_items: list, after_items: list):
    step = f"Verify removed items are not present in cart"
    with allure.step(step):
        allure.attach(format_items(before_items), name="Before removing", attachment_type=allure.attachment_type.TEXT)
        allure.attach(format_items(removed_items), name="Removed items", attachment_type=allure.attachment_type.TEXT)
        allure.attach(format_items(after_items), name="Items after remove", attachment_type=allure.attachment_type.TEXT)

        for item in removed_items:
            assert item not in after_items
