# CRUD-APP

A basic crud application allowing the aggregation of token values based on answers to questions. It is a dockerized application utilizing Flask, Vue, and Postgres.

## Requirements

* Docker

* Docker-Compose

The build process will import all needed dependencies for the Vue frontend and the Flask API.

## Usage

This project requires an `.env` file to run locally, the docker-compose file expects the following values:
`DB_USER`, `DB_PASSWORD`, `API_BASE_URL`

To run the application locally navigate to project root and enter `docker-compose up`

Frontend can be accessed at `http://localhost:8080`.

API can be accessed at `http://localhost:5000/api`.

Database can be administered at postgres default port: `5432`
