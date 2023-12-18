FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN chmod +x /app/inventory_task.py
CMD ./inventory_task.py