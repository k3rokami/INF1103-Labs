from Product import Product
from OrderLine import OrderLine
from DiscountStrategy import DiscountStrategy, NoDiscount

class Order:
    def __init__(self, order_id:str, discount: DiscountStrategy | None = None) -> None:
        self.order_id:str = order_id
        self.order_lines: list[OrderLine] = []
        self.discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def add_order_line(self, product:Product, quantity:int) -> None:
        order_line = OrderLine(product,quantity)
        self.order_lines.append(order_line)
    
    def calculate_total(self) -> float:
        total = sum(order_line.caculate_subtotal() for order_line in self.order_lines)
        return self.discount.apply(total)
    
    def remove_order_line(self, product_id:str) -> None:
        for order_line in self.order_lines:
            if product_id.lower() == order_line.product.get_product_id().lower():
                self.order_lines.remove(order_line)
                return None
