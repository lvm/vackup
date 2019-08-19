FROM python:3.7-alpine
LABEL author="mauro@sdf.org"

ARG UID=1000
ARG GID=1000

ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
ENV LANG C.UTF-8
ENV USER app
ENV HOME /app

COPY requirements.txt /app/requirements.txt

RUN pip install -U pip \
    && pip install -r /app/requirements.txt \
    && pip install gunicorn \
    && addgroup -S $USER -g $GID \
    && adduser -S -G $USER -u $UID -h $HOME $USER

COPY . /app

WORKDIR $HOME
EXPOSE 5000
USER $USER
