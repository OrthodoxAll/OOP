from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    all_products_count =0




    def __init__(self, name, description, products = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.category_count += 1
        Category.all_products_count += len(products) if products is not None else []

