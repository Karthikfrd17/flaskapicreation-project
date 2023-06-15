# Production-Quality API Endpoint

This repository contains a production-quality API endpoint implemented using Python and Flask. The API endpoint takes a sentence as input and returns a random 500-dimensional array of floats. It incorporates various features such as logging, error handling, input validation, authentication, and unit tests.

## Features

- API endpoint '/random_array' that accepts a sentence as input and returns a random 500-dimensional array of floats.
- Logging of important information and errors using the `logging` module.
- Error handling and input validation to ensure robustness and handle potential edge cases gracefully.
- Authentication mechanism to secure the API endpoints.
- Unit tests using the `unittest` library to validate the correctness and reliability of the API.
- Configuration settings stored in separate files for better management.
- Modular code structure with separate files for endpoints, tests, and configurations.

## Requirements

- Python 3.x
- Flask
- NumPy