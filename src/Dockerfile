# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

ENV PYTHONPATH=/app/src

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 8000 (or whichever port the app will run on)
EXPOSE 8000

# Command to run the application
CMD ["python", "start.py"]
