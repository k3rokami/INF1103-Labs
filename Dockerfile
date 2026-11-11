FROM python:3.11-slim
WORKDIR /app
COPY Inventory_Management_OOP.py Product.py Inventory.py CanBeShipped.py DigitalProduct.py PhysicalProduct.py Supplier.py Order.py OrderLine.py .
COPY data/inventory.json ./data/inventory.json
VOLUME /app/data
CMD ["python", "Inventory_Management_OOP.py"]