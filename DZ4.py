class Product:
    def __init__(self):
        self.name = "Tomato"
        self.price = 2
        self.quantity = 45
        self.calculate_total_price = (self.price * self.quantity)

    def display_info(self):
        print(f"Name product {self.name}. Cost Product {self.price}. Total price product {self.calculate_total_price}.")

product1 = Product
product1.display_info()


