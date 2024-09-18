# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
     build-essential \
     && rm -rf /var/lib/apt/lists/*

# Install Evidently
RUN pip install evidently

# Expose a port for the Evidently UI (if using the UI)
EXPOSE 8080


