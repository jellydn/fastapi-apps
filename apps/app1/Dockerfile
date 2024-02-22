# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Run the command to start uVicorn server
# Access http://fastapi-demo.traefik.me if you are using Traefik on your local machine
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

