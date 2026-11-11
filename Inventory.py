from Product import Product

class Inventory():
    def __init__(self):
        self.__products: list[Product] = []
        
    def get_products(self):
        return self.__products
    
    def find_product(self, product_id:str):
        for product in self.__products:
            if product_id.lower() == product.get_product_id().lower():
                return product
        return None
    
    def add_product(self, product: Product):
        for existing_product in self.__products:
            if existing_product.get_product_id() == product.get_product_id():
                print("Product ID already exists.")
                return None
        self.__products.append(product)

    def remove_product(self, product_id: str):
        for product in self.__products:
            if product.get_product_id().lower() == product_id.lower():
                self.__products.remove(product)
                return None
        print("Product not found")
        
    def search_product(self, product_id:str):
        for product in self.__products:
            if product_id.lower() == product.get_product_id().lower():
                return product
        return None
        # print("Product Found")
        # print("-" * 50)
        # print(f"ID: {product['id']}")
        # print(f"Name: {product['name']}")
        # print(f"Price: ${product['price']}")
        # print(f"Stock: {product['stock']}")
        # print("-" * 50)
        
    def update_stock(self, product_id:str, new_stock:int):
        product: Product | None = self.search_product(product_id)
        if product is None:
            print("Product not found.")
            return
        product.update_stock(new_stock)
        
    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return
        print("Current Inventory")
        print("-" * 48)
        for product in self.__products:
            product.display_information()
            # print(f"ID: {product.get_product_id()} | Name: {product.get_name()} | Price: {product.get_price()} | Stock: {product.get_stock()}")
        print("-" * 48)