#!/bin/bash

export GOOGLE_APPLICATION_CREDENTIALS="serviceAccount.json"
export SENTRY_SDK_DSN="https://36508a31dbb3468994b7ae470704ce10@o718840.ingest.sentry.io/5783806"

uvicorn main:app --reload
