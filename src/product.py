class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, product:dict, products:list[Product]):
        for existing in products or []:
            if existing.name == product["name"]:
                existing.quantity += product["quantity"]

                # повышать цену можно, понижать — нельзя: просто оставляем старую
                if product["price"] > existing.price:
                    existing.price = product["price"]

                return existing

        return cls(**product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            answer = input(
                f"Понизить цену с {self.__price} до {new_price}? (y/n): "
            )
            if answer.strip().lower() != "y":
                self.__price = new_price
                print(f"Установлена наовая цена {new_price}")
                return
            print(f"цена осталась прежней")


