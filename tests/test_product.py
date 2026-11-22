import pytest

from src.product import Product


def test_product_init(first_product: Product) -> None:
    """Проверяет корректность инициализации Product."""
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, gray"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_product_init_attributes_types(first_product: Product) -> None:
    """Проверяет типы атрибутов после инициализации."""
    assert isinstance(first_product.name, str)
    assert isinstance(first_product.description, str)
    assert isinstance(first_product.price, float)
    assert isinstance(first_product.quantity, int)


def test_product_price_is_private(first_product: Product) -> None:
    """Проверяет, что приватная цена недоступна напрямую."""
    with pytest.raises(AttributeError):
        _ = first_product.__price


def test_product_init_second_product(second_product: Product) -> None:
    """Проверяет инициализацию второго товара."""
    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


@pytest.mark.parametrize(
    ("name", "description", "price", "quantity"),
    [
        ("Samsung Galaxy S23 Ultra", "256GB, gray", 180000.0, 5),
        ("Iphone 15", "512GB, gray space", 210000.0, 8),
        ("Xiaomi Redmi Note 11", "1024GB, blue", 31000.0, 14),
        ("Телевизор", "Нет в наличии", 0.0, 0),
    ],
)
def test_product_init_with_different_values(
    name: str,
    description: str,
    price: float,
    quantity: int,
) -> None:
    """Проверяет инициализацию Product с разными наборами данных."""
    product = Product(
        name=name,
        description=description,
        price=price,
        quantity=quantity,
    )

    assert product.name == name
    assert product.description == description
    assert product.price == price
    assert product.quantity == quantity


def test_product_instances_are_independent(
    first_product: Product,
    second_product: Product,
) -> None:
    """Проверяет, что атрибуты разных товаров не пересекаются."""
    first_product.quantity = 1

    assert first_product.quantity == 1
    assert second_product.quantity == 8
    assert first_product is not second_product


def test_new_product() -> None:
    """Проверяет создание товара из словаря."""
    product = Product.new_product(
        {
            "name": "Iphone 15",
            "description": "512GB, gray space",
            "price": 210000.0,
            "quantity": 8,
        }
    )

    assert isinstance(product, Product)
    assert product.name == "Iphone 15"
    assert product.description == "512GB, gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_price_setter_positive(first_product: Product) -> None:
    """Проверяет обновление цены на положительное значение."""
    first_product.price = 200000.0

    assert first_product.price == 200000.0


def test_price_setter_lower_positive(first_product: Product) -> None:
    """Проверяет понижение цены на положительное значение."""
    first_product.price = 150000.0

    assert first_product.price == 150000.0


@pytest.mark.parametrize("new_price", [0, -100])
def test_price_setter_non_positive(
    first_product: Product,
    new_price: float,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Нулевая и отрицательная цена отклоняются с сообщением в консоль."""
    first_product.price = new_price

    assert first_product.price == 180000.0
    assert "Цена не должна быть нулевая или отрицательная" in capsys.readouterr().out
