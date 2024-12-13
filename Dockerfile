FROM python:3.14.0a1-slim

WORKDIR /app

COPY main.py .

CMD ["python", "main.py"]