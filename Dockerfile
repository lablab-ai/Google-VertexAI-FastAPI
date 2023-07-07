
# Step 1: Use official lightweight Python image as base OS.
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# ARG GOOGLE_APPLICATION_CREDENTIALS="/usr/src/app/serviceAccount.json"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies

# Bundle app source
COPY app /usr/src/app
ENV GOOGLE_APPLICATION_CREDENTIALS="./serviceAccount.json"
ENV SENTRY_SDK_DSN="https://36508a31dbb3468994b7ae470704ce10@o718840.ingest.sentry.io/5783806"

WORKDIR pdf2jsonl
RUN curl -fsSL https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs
RUN npm install
RUN sed -i 's/token in cache/token in cache \&\& typeof cache[token] === "string"/g' node_modules/gpt-3-encoder/Encoder.js

WORKDIR ..
# Step 3. Install production dependencies.
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
