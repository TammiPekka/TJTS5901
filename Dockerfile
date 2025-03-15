# Use an official Python runtime as a parent image
FROM python:3.9-slim AS builder

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only the dependencies file to take advantage of Docker caching
COPY requirements.txt .

# Install dependencies in a temporary layer
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.9-slim

WORKDIR /usr/src/app

# Copy only the necessary runtime dependencies from the build stage
COPY --from=builder /install /usr/local

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "app/app.py"]