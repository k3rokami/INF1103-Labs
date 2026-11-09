
from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from Inventory import Inventory

# 1. Create Supplier
supplier1 = Supplier("S001", "ABC Company", "abc@gmail.com")

# 2. Create Product BEFORE creating Inventory
product1 = PhysicalProduct(
    2, "P001", "Keyboard", 50.0, 10, supplier1
)

# 3. Create Inventory A and Inventory B
inventory_A = Inventory()
inventory_B = Inventory()

# 4. Add Product to Inventory A
print("Adding product to Inventory A...")
inventory_A.add_product(product1)

inventory_A.display_all()

# 5. Remove Product from Inventory A
print("\nRemoving product from Inventory A...")
inventory_A.remove_product("P001")

inventory_A.display_all()

# 6. Check whether Product still exists
print("\nChecking whether product still exists...")
product1.display_information()

# 7. Add the SAME Product to Inventory B
print("\nAdding the same product to Inventory B...")
inventory_B.add_product(product1)

inventory_B.display_all()

# 8. Confirm both variables reference the same object
print("\nAre they the same object?")
print(product1 is inventory_B.find_product("P001"))
