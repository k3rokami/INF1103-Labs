from Product import Product
from Supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, download_size, product_id, name, price, stock, supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size
        
    def display_information(self) -> None:
        super().display_information()
        self.supplier.display_information()
        print(f"Download Size: {self.__download_size} mb")
        # print("="*50)
        # print(f"ID: {self.get_product_id()}")
        # print(f"Name: {self.get_name()}")
        # print(f"Price: {self.get_price()}")
        # print(f"Stock: {self.get_stock()}")
        # print(f"Download Size: {self.__download_size} mb")
        # print("="*50)
    
    def get_fulfillment_info(self):
            return "This product is delivered digitally"

    def get_download_size(self):
        return self.__download_size
    

