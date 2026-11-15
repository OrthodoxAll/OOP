import json
from pathlib import Path

import pytest

from src.category import Category
from src.product import Product
from src.utils import (
    DEFAULT_PRODUCTS_PATH,
    creat_object_from_json,
    read_json,
)


@pytest.fixture(autouse=True)
def reset_category_counters() -> None:
    """Сбрасывает счётчики перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


def test_read_json_returns_list(tmp_path: Path) -> None:
    """Проверяет чтение JSON-файла."""
    path = tmp_path / "products.json"
    data = [
        {
            "name": "Test category",
            "description": "Test description",
            "products": [],
        }
    ]
    path.write_text(json.dumps(data), encoding="utf-8")

    assert read_json(path) == data


def test_creat_object_from_json(tmp_path: Path) -> None:
    """Проверяет создание объектов Category и Product из JSON."""
    path = tmp_path / "products.json"
    data = [
        {
            "name": "Smartphones",
            "description": "Mobile phones",
            "products": [
                {
                    "name": "Iphone 15",
                    "description": "512GB, gray space",
                    "price": 210000.0,
                    "quantity": 8,
                }
            ],
        }
    ]
    path.write_text(json.dumps(data), encoding="utf-8")

    categories = creat_object_from_json(read_json(path))

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert len(categories[0].products) == 1
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].name == "Iphone 15"
    assert categories[0].products[0].price == 210000.0
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_load_products_from_default_file() -> None:
    """Проверяет загрузку данных из data/products.json."""
    categories = creat_object_from_json(read_json(DEFAULT_PRODUCTS_PATH))

    assert len(categories) == 2
    assert sum(len(category.products) for category in categories) == 4
    assert all(isinstance(category, Category) for category in categories)
    assert all(isinstance(product, Product) for category in categories for product in category.products)
