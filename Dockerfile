FROM ubuntu:latest
LABEL authors="asala"

ENTRYPOINT ["top", "-b"]

# Start with a Python base image
FROM python:3.9-slim

# Prevent Python from writing .pyc files
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system tools needed for PostgreSQL
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all project files into the container
COPY . .