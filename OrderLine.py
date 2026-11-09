from Product import Product

class OrderLine():
    def __init__(self, product: Product, quantity):
        self.product:Product = product
        self.quantity = quantity
        
    def caculate_subtotal(self) -> float:
        return self.product.get_price() * self.quantity