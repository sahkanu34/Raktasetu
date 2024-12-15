# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install django mysql-connector pillow mysqlclient

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable to ensure output is sent to terminal
ENV PYTHONUNBUFFERED=1

# Run django server  when the container launches
CMD ["python", "manage.py", "runserver"]