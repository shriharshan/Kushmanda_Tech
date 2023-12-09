# FastAPI Web Service 🚀

This repository contains a FastAPI web service for image classification using a pre-trained TensorFlow model. The service receives image uploads, predicts the class using a deep learning model, and saves the prediction to a MySQL database.

## Table of Contents 📑

- [Files](#files)
- [Setup](#setup)
- [Usage](#usage)
- [Deployment](#deployment)

## Files 📂

- **api/api.py:** FastAPI router handling image predictions.
- **database/database.py:** Database model and functions for saving predictions.
- **main.py:** FastAPI application setup with CORS middleware and router inclusion.
- **Dockerfile:** Dockerfile for containerizing the application.
- **kubernetes.yaml:** Kubernetes deployment and service configuration.

## Setup ⚙️

### Clone the Repository:
   ```bash
   git clone https://github.com/shriharshan/Kushmanda_Tech.git
   cd your-repo
   ```


### Install Dependencies:
```
pip install -r requirements.txt
```

### Database Configuration:

Update the `DATABASE_URL` in `database/database.py` based on your MySQL configuration.

## Usage ▶️
### Run Locally:
```
uvicorn main:app --reload
```
Access the FastAPI Swagger documentation at `http://localhost:8000/docs` for API details.

### Upload an Image:
Use the `/net/image/prediction/` endpoint to upload an image and receive a prediction.

## Deployment 🚢
### Docker Deployment

1. ### Build Docker Image:
```
docker build -t your-docker-image-name .
```

2. Run Docker Container:
```
docker run -p 8000:8000 your-docker-image-name
```

### Kubernetes Deployment
Apply Kubernetes Configuration:

```
kubectl apply -f kubernetes.yaml
```

### Access the Service 🌐

After applying the Kubernetes configuration, the FastAPI web service can be accessed through the Kubernetes service.

###  Get Service Information:
```
kubectl get service fastapi-app-service
```

Use the external IP and port provided by the service to access the FastAPI web service.

```
curl http://EXTERNAL_IP:PORT
```
Replace `fastapi-app-service` with the actual name of your service, and `EXTERNAL_IP` and `PORT` with the values provided by the `kubectl get service` command.