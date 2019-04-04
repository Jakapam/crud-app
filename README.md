# CRUD-APP

A basic crud application allowing the aggregation of token values based on answers to questions. It is a dockerized application utilizing Flask, Vue, and Postgres.

## Requirements

* Docker (Confirmed on 2.0.0.3)

* Docker-Compose

The build process will import all needed dependencies for the Vue frontend and the Flask API.

## Usage

This project requires an `.env` file to run locally, the docker-compose expects the following values in the file:
`DB_USER`, `DB_PASSWORD`, `API_BASE_URL`,`JWT_SECRET`, and `FLASK_SECRET`.

To run the application locally navigate to project root and enter `docker-compose up`. Entrypoint for django app will generate mockdata, including an admin user `admin` with password `admin`.

Frontend can be accessed at `http://localhost:8080`.

API can be accessed at `http://localhost:5000/api`. This should also be the value passed to `API_BASE_URL` in the .env file when running locally.

Database can be administered at postgres default port: `5432`
