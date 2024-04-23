# CodingChallenge-ML-API


## Overview

This repository contains a machine learning API built for a coding challenge. The API provides endpoints for prediction based on a pre-trained machine learning model.

## Running the Project

### Using Docker

#### Build the Docker Image

Navigate to the project directory and run the following command to build the Docker image:

```bash
docker image build -t IMAGE_NAME:version .
```

This command builds the Docker image using a multistage build process. The first stage uses the 'alpine' base image to create a lightweight environment for building the Python dependencies with Poetry. The second stage uses the 'slim-bullseye' base image to install the 'scikit-learn' library along with 'gcc' and 'g++' for building the required packages.

Multistage builds offer the advantage of reducing the image size by discarding unnecessary build artifacts, resulting in a smaller and more efficient image.

#### Run the Docker Container

Once the image is built, run the Docker container using the following command:

```bash
docker container run -dit -p 8080:80 IMAGE_NAME:version
```

This command starts the Docker container in detached mode, mapping port 8080 on the host to port 80 on the container.

## Endpoint

### Local Endpoint

After running the Docker container, you can access the local API endpoints as follows:

- Prediction Endpoint: [http://localhost:8080/api/v1/predict](http://localhost:8080/api/v1/predict) 
- or [http://127.0.0.1:8080/api/v1/predict](http://127.0.0.1:8080/api/v1/predict)

- API Documentation: [http://localhost:8080/docs](http://localhost:8080/docs)

The API documentation provides details about the available endpoints, request/response formats, and example requests.

## Tests

The project includes asynchronous tests to validate the API endpoints. These tests focus on verifying the functionality of the routes. Future improvements could include performance testing, data structure validation, and additional metric analysis to ensure robustness and reliability.

## Observations

- **Machine Learning Model**: The machine learning model used in this project can be further optimized by implementing techniques such as cross-validation, feature selection, and tuning model parameters. You can refine the model by analyzing additional metrics and conducting thorough validations.

- **Jupyter Notebook**: The machine learning code used in this project can be found in the accompanying Jupyter notebook. This notebook serves as a starting point and can be enhanced by incorporating advanced machine learning techniques and best practices.
