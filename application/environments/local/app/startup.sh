#!/bin/sh
DEBUG=""

if [ "$APP_ENVIRONMENT" = "development" ]; then
  DEBUG="--reload"
fi

gunicorn -b 0.0.0.0:5000 $DEBUG application:app.app
