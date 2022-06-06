FROM python:3.10.0-alpine

RUN apk update && \
    apk add build-base libpq-dev

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt
