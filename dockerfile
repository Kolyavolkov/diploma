# syntax=docker/dockerfile:1
LABEL maintaner="Volkov Nikolai"
FROM python:3.9-alpine
WORKDIR .
RUN apk add --no-cache zlib-dev jpeg-dev gcc musl-dev linux-headers libffi-dev build-base
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3", "run.py"]
