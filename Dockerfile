FROM python:3.11-slim
WORKDIR /app
COPY . .
VOLUME /app/data
CMD ["python", "Inventory_Management_OOP.py"]
