class Inventory:
    def __init__(self):
        self.__products=[]
    
    def get_products(self):
        return self.__products
    
    def find_product(self, product_id):
        for product in self.__products:
            if product.get_product_id().lower() == product_id.lower():
                return product
        return None
    
    def add_product(self, product):
        if self.find_product(product.get_product_id()):
            print("Product ID already exists.")
            return
        self.__products.append(product)
        
    # def search_product(self, inventory, product_id):
    #     product=self.find_product(inventory, product_id)
    #     if product == None:
    #         print("Product is not found.")
    #         return
    #     print("Product Found")
    #     print("-" * 50)
    #     print(f"ID: {product['id']}")
    #     print(f"Name: {product['name']}")
    #     print(f"Price: ${product['price']}")
    #     print(f"Stock: {product['stock']}")
    #     print("-" * 50)
        
    def display_all(self):
        print("Current Inventory")
        print("-" * 48)
        if not self.__products:
            print("Inventory is empty.")
        for product in self.__products:
            product.display_information()
        print("-" * 48)

    # def search_product(self, product_id):
    #     product = self.find_product(product_id)
    #     if product is None:
    #         print("Product is not found.")
    #         return
    #     print("Product Found")
    #     print("-" * 50)
    #     product.display_information()
    #     print("-" * 50)

    # def update_stock(self, product_id, new_stock):
    #     product = self.find_product(product_id)
    #     if product is None:
    #         print("Product is not found.")
    #         return False
    #     return product.update_stock(new_stock)
