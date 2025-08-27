# Stage 1: Preprocess with Python
FROM python:3.11-slim as builder

WORKDIR /app
COPY books.csv /app/books.csv
COPY preprocessing.py /app/preprocessing.py

RUN pip install pandas numpy
RUN python preprocessing.py

# Stage 2: Import with mongo tools
FROM mongo:latest

WORKDIR /app
COPY --from=builder /app/books_cleaned.json /app/books_cleaned.json

CMD bash -c "mongoimport --host mongodb --db becode --collection books --file /app/books_cleaned.json --jsonArray"