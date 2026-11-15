import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product() -> Product:
    """Первый товар для тестов."""
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, gray",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product() -> Product:
    """Второй товар для тестов."""
    return Product(
        name="Iphone 15",
        description="512GB, gray space",
        price=210000.0,
        quantity=8,
    )


@pytest.fixture
def third_product() -> Product:
    """Третий товар для тестов."""
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, blue",
        price=31000.0,
        quantity=14,
    )


@pytest.fixture
def fourth_product() -> Product:
    """Четвёртый товар для тестов."""
    return Product(
        name="55 QLED 4K",
        description="4K TV",
        price=123000.0,
        quantity=7,
    )


@pytest.fixture
def fifth_product() -> Product:
    """Пятый товар для тестов."""
    return Product(
        name="65 QLED 4K",
        description="4K TV",
        price=150000.0,
        quantity=3,
    )


@pytest.fixture
def first_category(
    first_product: Product,
    second_product: Product,
    third_product: Product,
) -> Category:
    """Первая категория с тремя товарами."""
    return Category(
        name="Smartphones",
        description="Mobile phones",
        products=[first_product, second_product, third_product],
    )


@pytest.fixture
def second_category(
    fourth_product: Product,
    fifth_product: Product,
) -> Category:
    """Вторая категория с двумя товарами."""
    return Category(
        name="TVs",
        description="Televisions",
        products=[fourth_product, fifth_product],
    )
