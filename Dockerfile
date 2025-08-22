FROM python:3.14.0rc2-slim

WORKDIR /app

COPY main.py .

CMD ["python", "main.py"]