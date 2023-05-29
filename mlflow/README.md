based on: https://github.com/bubulmet/mlflow-postgres-minio

### Build & Launch

```bash
docker compose up -d --build
```

#### Get IP address of the mlflow container

```bash
docker inspect mlflow-mlflow-1 -f '{{json .NetworkSettings.Networks.mlflow_default.IPAddress}}'
```
The container is available on :5000

#### Get IP address of the minio container

```bash
docker inspect mlflow-minio-1 -f '{{json .NetworkSettings.Networks.mlflow_default.IPAddress}}'
```
The MinIO admin console is available on :9001
