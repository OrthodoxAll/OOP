import json
from pathlib import Path
from typing import Any

from src.category import Category
from src.product import Product

DEFAULT_PRODUCTS_PATH = Path(__file__).resolve().parent.parent / "data" / "products.json"


def read_json(path: str | Path) -> list[dict[str, Any]]:
    """Читает JSON-файл и возвращает список словарей."""
    with open(path, "r", encoding="utf-8") as file:
        data: list[dict[str, Any]] = json.load(file)
        return data


def creat_object_from_json(data: list[dict[str, Any]]) -> list[Category]:
    """Создаёт категории и товары из данных JSON."""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    raw_data = read_json(DEFAULT_PRODUCTS_PATH)
    categories_data = creat_object_from_json(raw_data)
    print(categories_data[0].name)
    print(categories_data[1].name)
