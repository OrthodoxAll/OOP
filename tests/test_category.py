import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counters() -> None:
    """Сбрасывает счётчики перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


def test_category_init(
    first_category: Category,
    first_product: Product,
    second_product: Product,
    third_product: Product,
) -> None:
    """Проверяет корректность инициализации Category."""
    assert first_category.name == "Smartphones"
    assert first_category.description == "Mobile phones"
    assert first_category.products == [
        first_product,
        second_product,
        third_product,
    ]
    assert all(isinstance(product, Product) for product in first_category.products)


def test_category_init_attributes_types(first_category: Category) -> None:
    """Проверяет типы атрибутов после инициализации."""
    assert isinstance(first_category.name, str)
    assert isinstance(first_category.description, str)
    assert isinstance(first_category.products, list)


def test_category_init_empty_products_list() -> None:
    """Проверяет создание категории с явно пустым списком товаров."""
    category = Category("Empty", "No products", [])

    assert category.name == "Empty"
    assert category.description == "No products"
    assert category.products == []


def test_category_count(
    first_category: Category,
    second_category: Category,
) -> None:
    """Проверяет подсчёт количества категорий."""
    assert first_category.category_count == 2
    assert second_category.category_count == 2
    assert Category.category_count == 2


def test_category_count_increases_on_creation() -> None:
    """Проверяет, что счётчик категорий растёт при каждом создании."""
    assert Category.category_count == 0

    Category("First", "First category")
    assert Category.category_count == 1

    Category("Second", "Second category")
    assert Category.category_count == 2


def test_product_count(
    first_category: Category,
    second_category: Category,
) -> None:
    """Проверяет подсчёт количества продуктов."""
    assert first_category.product_count == 5
    assert second_category.product_count == 5
    assert Category.product_count == 5


def test_product_count_increases_on_creation(
    first_product: Product,
    second_product: Product,
) -> None:
    """Проверяет, что счётчик продуктов учитывает товары каждой категории."""
    assert Category.product_count == 0

    Category("First", "First category", [first_product])
    assert Category.product_count == 1

    Category("Second", "Second category", [first_product, second_product])
    assert Category.product_count == 3


def test_category_without_products() -> None:
    """Проверяет создание категории без товаров."""
    category = Category("Empty", "No products")

    assert category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0
