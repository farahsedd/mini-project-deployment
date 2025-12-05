FROM python:3.14.1-slim

WORKDIR /app

COPY main.py .

CMD ["python", "main.py"]