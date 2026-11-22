from src.product import Product


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] | None = None) -> None:
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

        for product in products or []:
            self.add_product(product)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в приватный список и увеличивает счётчик продуктов."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает все товары категории в виде строки."""
        return "".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n" for product in self.__products
        )
