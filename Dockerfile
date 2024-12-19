# Use slim variant of Python image to reduce base image size
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Expose port
EXPOSE 8000:8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]