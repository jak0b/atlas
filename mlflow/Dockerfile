FROM python:3.11.3-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -vf /app/requirements.txt

CMD mlflow server \
  --backend-store-uri ${BACKEND_STORE_URI} \
  --default-artifact-root ${DEFAULT_ARTIFACT_ROOT} \
  --host 0.0.0.0
