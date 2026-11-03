from Product import Product

class DigitalProduct(Product):
    def __init__(self, download_size, product_id, name, price, stock):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size
        
    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size} mb")
        # print("="*50)
        # print(f"ID: {self.get_product_id()}")
        # print(f"Name: {self.get_name()}")
        # print(f"Price: {self.get_price()}")
        # print(f"Stock: {self.get_stock()}")
        # print(f"Download Size: {self.__download_size} mb")
        # print("="*50)
        
