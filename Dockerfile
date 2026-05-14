<<<<<<< HEAD
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

=======
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

>>>>>>> 27283fbbfb3921e303e62e06505444af1a18331f
CMD ["python", "app.py"]