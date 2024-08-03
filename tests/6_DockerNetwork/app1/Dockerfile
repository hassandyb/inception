# Dockerfile for app1
FROM python:3.9-alpine

# Install required Python libraries
RUN pip install --no-cache-dir requests

COPY app1.py /app/app1.py

CMD ["python", "/app/app1.py"]
