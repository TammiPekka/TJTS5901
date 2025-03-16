# Use an official Python runtime as a parent image
FROM python:3.9-slim AS builder

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only the dependencies file to take advantage of Docker caching
COPY requirements.txt .

# Install dependencies in a temporary layer
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim

WORKDIR /usr/src/app

# Copy all installed libraries and dependencies from the builder stage
COPY --from=builder /usr/local /usr/local

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app.app:app"]
