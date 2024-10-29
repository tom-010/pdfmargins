# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the project files into the container
# install gcc
RUN apt-get update && apt-get install -y gcc g++
# clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install the project dependencies
RUN poetry install --with api

RUN apt remove -y gcc g++


# Set the entry point for the application
CMD ["./.venv/bin/uvicorn", "pdfmargins.api:app", "--host", "0.0.0.0", "--port", "8000"]