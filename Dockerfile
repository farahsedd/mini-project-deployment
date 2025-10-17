FROM python:3.14.0-slim

WORKDIR /app

COPY main.py .

CMD ["python", "main.py"]