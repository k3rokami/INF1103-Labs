FROM python:3.11-slim
WORKDIR /app
COPY Inventory_Management_OOP.py .
RUN mkdir -p /app/data
VOLUME /app/data
CMD ["python", "Inventory_Management_OOP.py"]