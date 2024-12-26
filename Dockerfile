# Use slim variant of Python image to reduce base image size
FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

RUN pip install --upgrade pip


COPY . /requirements.txt

#pip install mysqlclient pillow

COPY . .

# Expose port
EXPOSE 8000:8000

# Command to run the application
CMD ["python", "manage.py", "runserver"]