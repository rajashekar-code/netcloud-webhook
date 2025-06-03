FROM python:3.10-slim
WORKDIR /app
COPY webhook.py /app/
RUN pip install flask
CMD ["python", "webhook.py"]
