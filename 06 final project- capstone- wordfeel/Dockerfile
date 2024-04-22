FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set working directory
WORKDIR /usr/src/app

# Install dependencies
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the Django project files
COPY . .

# Import the database dump
COPY ./etymwn-dump.sql .

# Command to run the server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]