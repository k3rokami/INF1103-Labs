from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from Order import Order


supplier1 = Supplier("S001", "ABC Supplies", "abc@email.com")
product1 = PhysicalProduct(0.5, "P001", "Keyboard", 50.0, 20, supplier1)
product2 = PhysicalProduct(0.2, "P002", "Mouse", 25.0, 30, supplier1)

order1 = Order("O001")
order2 = Order("O002")

order1.add_order_line(product1, 2)
order1.add_order_line(product2, 3)

order2.add_order_line(product1, 5)

print("="*10+"ORDER 1"+"="*10)

for order_line in order1.order_lines:
    print(
        f"{order_line.product.get_name()} "
        f"x {order_line.quantity} "
        f"= ${order_line.caculate_subtotal():.2f}"
    )

print(f"Total: ${order1.calculate_total():.2f}")

print("="*10+"ORDER 2"+"="*10)

for order_line in order2.order_lines:
    print(
        f"{order_line.product.get_name()} "
        f"x {order_line.quantity} "
        f"= ${order_line.caculate_subtotal():.2f}"
    )

print(f"Total: ${order2.calculate_total():.2f}")


print("Same Product object:",
    order1.order_lines[0].product is order2.order_lines[0].product)

print("Same OrderLine object:",
    order1.order_lines[0] is order2.order_lines[0])

print("\nRemove orderline from order 1")
order1.remove_order_line("P001")

for order_line in order1.order_lines:
    print(
        f"{order_line.product.get_name()} "
        f"x {order_line.quantity}"
    )

print(f"New Order 1 Total: ${order1.calculate_total():.2f}")

for order_line in order2.order_lines:
    print(
        f"{order_line.product.get_name()} "
        f"x {order_line.quantity}"
    )

print(f"Order 2 Total: ${order2.calculate_total():.2f}")