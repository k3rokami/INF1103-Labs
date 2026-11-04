from Product import Product
from CanBeShipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, weight, product_id, name, price, stock):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight
        
    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfillment_info(self):
        return "This product requires Physical Shipping"
    
    def calculate_shipping_cost(self):
        return self.__weight *2
    
    def get_weight(self):
        return self.__weight