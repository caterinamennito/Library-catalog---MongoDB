# Library Catalog — MongoDB

This project is a containerized library catalog system using MongoDB and Python. It demonstrates how to preprocess book data, seed a MongoDB database, and perform queries and aggregations using Jupyter notebooks.

## Features
- Preprocesses raw book data (CSV) into clean JSON for MongoDB import
- Seeds a MongoDB database with the cleaned data using Docker Compose and multi-stage builds
- Provides example queries and aggregations in a Jupyter notebook (`books.ipynb`)
- Supports advanced MongoDB queries (e.g., regex, aggregation, unwinding arrays)

## Project Structure

- `books.csv` — Raw book data
- `mongo-seed/preprocessing.py` — Cleans and transforms the CSV for MongoDB
- `mongo-seed/Dockerfile` — Multi-stage build: preprocesses data, then imports into MongoDB
- `docker-compose.yml` — Orchestrates MongoDB and the seed process
- `books.ipynb` — Example queries and analysis in Python
- `requirements.txt` — Python dependencies

## Setup & Usage

1. **Clone the repository**
2. **Build and run the containers:**
	```sh
	docker-compose build --no-cache
	docker-compose up
	```
	This will preprocess the data and import it into MongoDB.

3. **Run and explore the Jupyter notebook:**
	- Open `books.ipynb` in VS Code or Jupyter Lab
	- Try the example queries and aggregations

## Example Queries

- Find all books by a specific author (exact or regex match)
- Find all books in a genre
- Calculate average rating for a genre
- Find the genre with the highest average rating (using `$unwind` and `$group`)