#!/bin/sh

gunicorn --bind $HOST:$PORT --workers $WORKERS app:app
