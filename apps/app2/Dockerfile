FROM python:3.12 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

# Generate requirements.txt from pyproject.toml
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.12-slim

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt 

COPY ./fastapi_app_demo /code/app

# Run the command to start uVicorn server
# Access http://fastapi-app-demo.traefik.me if you are using Traefik on your local machine
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
