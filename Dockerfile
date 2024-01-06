# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE "gymbuddy.settings"

# Create and set the working directory
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install pip install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local project directory into the container
COPY . .

# Port number the container should expose
EXPOSE 8000

# Command to run on container start
CMD ["gunicorn", "gymbuddy.wsgi.application", "--bind", "0.0.0.0:8000"]

