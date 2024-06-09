# CONTRIBUTING

## How to run Dockerfile locally

```
docker run -dp 5005:5000 -w /app -v "${PWD}:/app" IMAGE_NAME

```

## How to build docker file

```
 docker build -t flask-api2 .   
```