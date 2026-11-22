import pytest

from src.category import Category
from src.product import Product
from tests.helpers import get_private_products


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
    assert get_private_products(first_category) == [
        first_product,
        second_product,
        third_product,
    ]
    assert all(isinstance(product, Product) for product in get_private_products(first_category))


def test_category_init_attributes_types(first_category: Category) -> None:
    """Проверяет типы атрибутов после инициализации."""
    assert isinstance(first_category.name, str)
    assert isinstance(first_category.description, str)
    assert isinstance(first_category.products, str)
    assert isinstance(get_private_products(first_category), list)


def test_category_products_is_private(first_category: Category) -> None:
    """Проверяет, что приватный список недоступен напрямую."""
    with pytest.raises(AttributeError):
        _ = first_category.__products


def test_category_init_empty_products_list() -> None:
    """Проверяет создание категории с явно пустым списком товаров."""
    category = Category("Empty", "No products", [])

    assert category.name == "Empty"
    assert category.description == "No products"
    assert category.products == ""
    assert get_private_products(category) == []


def test_products_getter_format(first_category: Category) -> None:
    """Проверяет формат строки, возвращаемой геттером products."""
    assert first_category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_add_product(first_product: Product, second_product: Product) -> None:
    """Проверяет добавление товара и увеличение счётчика продуктов."""
    category = Category("Smartphones", "Mobile phones")

    assert category.add_product(first_product) is None  # type: ignore[func-returns-value]
    assert category.add_product(second_product) is None  # type: ignore[func-returns-value]
    assert get_private_products(category) == [first_product, second_product]
    assert Category.product_count == 2
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n" in category.products


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

    assert category.products == ""
    assert get_private_products(category) == []
    assert Category.category_count == 1
    assert Category.product_count == 0
