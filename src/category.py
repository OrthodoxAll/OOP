from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(products) if products is not None else 0

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "".join(f'{Product.name}, 80 руб. Остаток: {Product.quantity} шт.\n'
        for Product in self.__products)

