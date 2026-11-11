from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier
from Inventory import Inventory
from Order import Order
from Product import Product

supplier = Supplier("S001", "ABC Company", "abc@gmail.com")
product = PhysicalProduct(2, "P001", "Keyboard", 50, 10, supplier)

# product.supplier.display_information()

# digital = DigitalProduct(500, "P002", "E-Book", 15.0, 20, supplier)
# digital.supplier.display_information()
# del supplier
# test=DigitalProduct(50,"P001","idk",120,30, supplier)
# test.display_information()

# inventory_A = Inventory()
# inventory_B = Inventory()

# inventory_A.add_product(product)
# inventory_A.display_all()
# inventory_A.remove_product("P001")
# inventory_A.display_all()
# inventory_B.add_product(product)
# inventory_B.display_all()


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfillment_info())

digital = DigitalProduct(500, "P002", "E-Book", 15.0, 20, supplier)

test_inventory = Inventory()
test_inventory.add_product(product)
test_inventory.add_product(digital)

for item in test_inventory.get_products():
    show_product_details(item)