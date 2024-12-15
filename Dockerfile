# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --upgrade pip

RUN pip install mysqlclient mysql-connector django pillow 

EXPOSE 8000:8000

ENV PYTHONUNBUFFERED=1

ENV DJANGO_SETTINGS_MODULE=your_project_name.settings.production


CMD ["python", "manage.py", "runserver"]