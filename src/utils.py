import json
from pathlib import Path

from src.category import Category
from src.product import Product


DEFAULT_PRODUCTS_PATH = (
    Path(__file__).resolve().parent.parent / "data" / "products.json"
)

def read_json(path:str)->dict:

    with open(path, "r",encoding='UTF=8') as file:
        data = json.load(file)
        return data


def creat_object_from_json(data):
    categoryes = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categoryes.append(Category(**category))

    return categoryes

if __name__ == "__main__":
    raw_data = read_json(DEFAULT_PRODUCTS_PATH)
    # print(raw_data)
    categoryes_data = creat_object_from_json(raw_data)
    print(categoryes_data[0].name)
    print(categoryes_data[1].name)