from Product import Product

class PhysicalProduct(Product):
    def __init__(self, weight, product_id, name, price, stock):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight
        
    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

