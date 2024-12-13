FROM python:3.14.0a2-alpine3.21

WORKDIR /app

COPY main.py .

CMD ["python", "main.py"]