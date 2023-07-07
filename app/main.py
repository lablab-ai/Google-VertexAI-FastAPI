from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.auth import credentials
from google.oauth2 import service_account
import google.cloud.aiplatform as aiplatform
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
import vertexai


# Load the service account json
service_account_info = {
    "type": "service_account",
    "project_id": "loyal-flames-391709",
    "private_key_id": "610c66317a1ec89474a773c41683d4faf5599f6d",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDCiY6GtwWTqvly\ndJHTm1rKf5LLsJ/qormtAp07zcV4rEojmJYv+8ca3/Ety2P7oh9DY/pq4tubntvf\nSGAkpT3Enhzw8ZoYhBQX8tdKczHmF6j3s7blLF5kU0uB8fGiwtm3RAmj1P3ztEuN\nhATY+342hgUnh6T4NcIETEPRYxF8sgbjbkMWm5rMrFy7r/hhDjmRdPV0iuIvu48D\n5e2gXYmzdHUZgxU91+WN8zln6IQ1lVNGTZyhNq/SfZF0PnTbSD+CnXRR7iPK55dy\npYC6Bb6LTJsG9ST0AA7AndajgXFQRb9VBLPwmcdsyg3MbbM/J2ZxDFgWAuZxYj4m\nOhr6cpntAgMBAAECggEACbFDU+RyB2+1EnYK3vVmUmEFThc8fHsDj8Jp1ZU0wcSp\nw/jCAN2FR8pBELRJxLuI3blxPFqVsPz6/Pa07ZZ7C50KGZocAJ0yCBhuEBRJt+pV\nXZQLaIMrp8l7oVuN27tkEAy4gzxlM7t3qTMa77mmCe7m+ld4iXJaOo8XMOtD74ez\nxpJcwzPxwOzdF3WCNEoXsZfxNBln+wZ9FALRh7P1LpNrsxrbcyUGW2/LPz/xHKHc\nUDahNVOQYZwRuGjLiqiWLNOSy1vLfILydS/S17jc5FWD20Eykt0wiusR135dDhh6\nvvRzJ54Dbg8vrXn3vlsRI/lNeysgMTsdZtnmgwOlAQKBgQD8bCWVeC0HconcqAsE\n3IVhURHnxfpcJ//lYyDKlqQYy7769oIqM9yn5/oHmv+5Tu63N8Ql12fuAEZ79JKR\nD51k6l+FDI/xCQkpkpX7aU7L0z0LnJIqComvm588mPPSk0Y7Dpzdmg78UAc6cahB\ns7JoA7HkB4Jxyq0I75w3PWnTAQKBgQDFS2NO9rcZqfAqUc8KOxGeARs773jmHc4y\nSBYuWH/EKipkH6C8J6OCctMErVGCKIebK0GEbv9eiCY9s2A8gqVl/8ViE1JBFKp4\nmxCiu1gNz5Gh+b1AzUuwfz7Kw0As4hRJL2YpolzYtZNk0MYDqNVKZRYhTmj8QfAi\nu57cWxRC7QKBgA//4tn4hhIkxmxAEoK6X5Hti47/U4En3+ZwRBHTPo97yp0pptJ5\n+xCBea2lu3PJdwQR+tLTNnk1d0JAHFIphTZyTJ+oTi9e/T+vVOZcpGvy9bmYsQMN\nK/D/kjZLE5lTUG5J3NOHAlAn2m1v6tRPSY2iPlJPz4ra5+DbHzG5KM4BAoGAGPHF\nJpCu6cHAqbkaMjLxsUZ2iQdoA8A098qBc26hCM5D+dC948wnMjEOWQMI0SoKqyW2\n7OWTyAHyw85QFpZ2DwVdkV7cAXp5azI/0jNZmLVrtkz7DpxmO3R7Heu9y27yHaau\nhgkPMB8U+aQjxQatoPBS8fcV8v7rO5j5JuclEqkCgYAfrwrUwtQsyqAyk725vDz/\nd8FeCVghUTN8IWj5FYIlrpSlj22wonsFEc7NhD3bSIXNw+qZSn3pMBvciCtaw2n6\nt88ojLvsSlMVlgToKSoaAe+Wm3fKdjUJ01qRdNp0P/XiLGpEfb6m4AJIlnc6Nrx1\nE3Nn2A2D22Y/Gz92hZj6OA==\n-----END PRIVATE KEY-----\n",
    "client_email": "test-327@loyal-flames-391709.iam.gserviceaccount.com",
    "client_id": "100923718079042582747",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/test-327%40loyal-flames-391709.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com",
}


my_credentials = service_account.Credentials.from_service_account_info(
    service_account_info
)

# Initialize Google AI Platform with project details and credentials
aiplatform.init(
    project="loyal-flames-391709",
    location="us-central1",
    staging_bucket="gs://my_staging_bucket",
    credentials=my_credentials,
    experiment="my-experiment",
    experiment_description="my experiment description",
)

# Initialize Vertex AI with project and location
vertexai.init(project="loyal-flames-391709", location="us-central1")

app = FastAPI()

# Configure CORS for the application
origins = ["http://localhost", "http://localhost:8080", "http://localhost:3000"]
origin_regex = r"https://(.*\.)?alexsystems\.ai"
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=origin_regex,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint that returns available endpoints in the application"""
    return {
        "Endpoints": {
            "chat": "/chat",
        }
    }


@app.get("/docs")
async def get_documentation():
    """Endpoint to serve Swagger UI for API documentation"""
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/redoc")
async def get_documentation():
    """Endpoint to serve ReDoc for API documentation"""
    return get_redoc_html(openapi_url="/openapi.json", title="redoc")


@app.post("/chat")
async def handle_chat(human_msg: str):
    """
    Endpoint to handle chat.
    Receives a message from the user, processes it, and returns a response from the model.
    """
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    parameters = {
        "temperature": 0.8,
        "max_output_tokens": 1024,
        "top_p": 0.8,
        "top_k": 40,
    }
    chat = chat_model.start_chat(  # Initialize the chat with model
        # chat context and examples go here
    )
    # Send the human message to the model and get a response
    response = chat.send_message(human_msg, **parameters)
    # Return the model's response
    return {"response": response.text}
