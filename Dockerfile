# Use a lightweight Python base image
FROM python:3.13.0-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the script
CMD ["python", "src/ols_lookup.py"]