# Getting started with Vertex AI Generative AI

## Before you begin

This is a simple starter boilerplate that gives you a basic FastAPI setup with a few endpoints. It is meant to be used as a starting point for your own projects.

### Clone and install dependencies

In your terminal, run the following commands:

```
git clone git@github.com:lablab-ai/Google-VertexAI-FastAPI.git
cd Google-VertexAI-FastAPI
cd app
pip install -r requirements.txt
```

### Update the project auth

In order to use the Vertex AI SDK, you will need to update the project auth using a serviceaccount

In `main.py`, update the following code with your service account data that you obtained from the GCP console or through the lablab.ai platform.

```
service_account_info = {
    "type": "service_account",
    "project_id": "YOUR_PROJECT_ID",
    "private_key_id": "YOUR_PRIVATE_KEY_ID",
    "private_key": "YOUR_PRIVATE_KEY",
    "client_email": "YOUR_CLIENT_EMAIL",
    "client_id": "YOUR_CLIENT_ID",
    "auth_uri": "YOUR_AUTH_URI",
    "token_uri": "YOUR_TOKEN_URI",
    "auth_provider_x509_cert_url": "YOUR_AUTH_PROVIDER_X509_CERT_URL",
    "client_x509_cert_url": "YOUR_CLIENT_X509_CERT_URL",
    "universe_domain": "YOUR_UNIVERSE_DOMAIN",
}

```
