from Product import Product
from OrderLine import OrderLine

class Order:
    def __init__(self, order_id:str):
        self.order_id:str = order_id
        self.order_lines: list[OrderLine] = []
        
    def add_order_line(self, product:Product, quantity:int) -> None:
        order_line = OrderLine(product,quantity)
        self.order_lines.append(order_line)
    
    def calculate_total(self) -> float:
        total = 0
        for order_line in self.order_lines:
            total += order_line.caculate_subtotal()
        return total
    
    def remove_order_line(self, product_id:str) -> None:
        for order_line in self.order_lines:
            if product_id.lower() == order_line.product.get_product_id().lower():
                self.order_lines.remove(order_line)
                return
