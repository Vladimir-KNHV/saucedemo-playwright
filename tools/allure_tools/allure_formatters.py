from typing import Iterable
from test_data.models.product_data import ProductItem

def format_items(items: Iterable[ProductItem]) -> str:
    return "\n\n".join(
        f"🛒 {i.name}\n"
        f"💬 {i.description}\n"
        f"💰 {i.price}"
        for i in items
    )

def format_sort_result(items: Iterable) -> str:
    result = [str(x) for x in items]
    return "\n".join(result)