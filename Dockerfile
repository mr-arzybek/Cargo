# Use the official Python 3.10 image as the base image
FROM python:3.10

# Set environment variables to control Python's behavior
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create and set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the rest of your application code into the container
COPY . /app/

# Install any additional dependencies if needed
# RUN pip install some-package

# Set the DJANGO_SETTINGS_MODULE environment variable
ENV DJANGO_SETTINGS_MODULE=core.settings.base

# Expose the port on which your application will run (change it if necessary)
EXPOSE 8000

# Define the default command to run when starting the container
# Here, we specify the IP and port to ensure the Django development server
# is accessible from outside the Docker container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
