FROM python:3.9

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install Python packages
RUN pip install mysqlclient mysql-connector-python django pillow

# Rest of your Dockerfile continues...

COPY . .

EXPOSE 8000:8000

CMD [ "python","manage.py","runserver" ]
