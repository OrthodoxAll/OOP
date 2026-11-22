from typing import cast

from src.category import Category
from src.product import Product


def get_private_products(category: Category) -> list[Product]:
    """Возвращает приватный список товаров категории для проверок в тестах."""
    return cast(list[Product], getattr(category, "_Category__products"))
