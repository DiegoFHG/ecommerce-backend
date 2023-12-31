FROM python:3.11.3-alpine3.18 as DEV

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt