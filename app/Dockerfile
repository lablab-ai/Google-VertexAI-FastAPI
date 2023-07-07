#########################################################
### THIS IS FOR LOCAL DEVELOPMENT NOT FOR PRODUCTIOPN ###
#########################################################
# Step 1: Use official lightweight Python image as base OS.
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7



RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV GOOGLE_APPLICATION_CREDENTIALS="/usr/src/app/serviceAccount.json"
ENV SENTRY_SDK_DSN="https://36508a31dbb3468994b7ae470704ce10@o718840.ingest.sentry.io/5783806"

WORKDIR pdf2jsonl
RUN curl -fsSL https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs
RUN npm install
RUN sed -i 's/token in cache/token in cache \&\& typeof cache[token] === "string"/g' node_modules/gpt-3-encoder/Encoder.js

WORKDIR ..
# Step 3. Install production dependencies.
RUN pip install -r requirements.txt
