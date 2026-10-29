FROM python:3.11-slim
WORKDIR /app
COPY persistent_auditor.py .
RUN mkdir -p /app/data
VOLUME /app/data
CMD ["python", "persistent_auditor.py"]