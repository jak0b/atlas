FROM python:3.11.3-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -vf /app/requirements.txt

COPY test /app/test
