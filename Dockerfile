# Use the official Python image as the base image
FROM python:3.10-slim-buster


# Set the working directory in the container
WORKDIR /code

# Copy requirements.txt (if available) to the container
COPY requirements.txt /code/

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /code/

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
