# Use an appropriate base image with Python installed
FROM python:3.12.2

# Install FreeTDS and its dependencies
RUN apt-get update && \
    apt-get install -y freetds-dev freetds-bin tdsodbc unixodbc-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port on which your Flask app will run
EXPOSE 3000

# Command to run your Flask application
CMD ["gunicorn", "-b", "0.0.0.0:3000", "app:app"]
