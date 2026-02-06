FROM python:3.14.3-slim

WORKDIR /app

COPY main.py .

CMD ["python", "main.py"]