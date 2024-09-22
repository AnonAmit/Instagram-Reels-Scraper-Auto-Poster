# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the src folder contents into the container at /app/src
COPY src/ ./src

# Set the Python path to include src/
ENV PYTHONPATH=/app/src

# Expose the port if necessary
EXPOSE 8000

# Command to run the application
CMD ["python", "src/start.py"]

