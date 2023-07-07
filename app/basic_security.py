import secrets
from fastapi.security import HTTPBasicCredentials
from fastapi import HTTPException, status


def verify_http_basic_credentials(credentials: HTTPBasicCredentials):
    correct_username = secrets.compare_digest(credentials.username, "alex")
    correct_password = secrets.compare_digest(credentials.password, "alex2021")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
