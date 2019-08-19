#!/bin/sh

celery flower -A $CELERY_MODULE --port=$FLOWER_PORT --broker=$CELERY_BROKER_URL
