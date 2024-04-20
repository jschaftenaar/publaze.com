# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory to /app
WORKDIR /app

# Update packages and install ca-certificates
RUN apt-get update && \
    apt-get install -y ca-certificates && \
    update-ca-certificates

# Install any needed packages specified in requirements.txt
# Assumes requirements.txt is in the same directory as Dockerfile
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Command to run the application
CMD ["flask", "run"]
