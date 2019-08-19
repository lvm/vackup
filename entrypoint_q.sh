#!/bin/sh

celery -A $CELERY_MODULE worker --loglevel=info
