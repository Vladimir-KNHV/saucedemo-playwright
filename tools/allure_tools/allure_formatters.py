from typing import Iterable

def format_items(items: Iterable) -> str:
    return "\n\n".join(
        f"🛒 {i.name}\n"
        f"💬 {i.description}\n"
        f"💰 {i.price}"
        for i in items
    )

def format_sorting(items: Iterable) -> str:
    result = [str(x) for x in items]
    return "\n".join(result)