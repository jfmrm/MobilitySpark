FROM python:3.8.0a4-alpine3.9

EXPOSE 8765

WORKDIR websocket

COPY . .

RUN apk add bash

RUN chmod +x wait-for-it.sh

RUN pip3 install websockets pika utm
