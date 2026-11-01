FROM python:3.11-slim
WORKDIR /app
COPY Inventory_Management_OOP.py .
COPY data/inventory.json ./data/inventory.json
VOLUME /app/data
CMD ["python", "Inventory_Management_OOP.py"]