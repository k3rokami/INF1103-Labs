FROM python:3.11-slim
WORKDIR /app
COPY Inventory_Management_OOP.py Product.py Inventory.py .
COPY data/inventory.json ./data/inventory.json
VOLUME /app/data
CMD ["python", "Inventory_Management_OOP.py"]