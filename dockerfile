# syntax=docker/dockerfile:1
FROM python:3.9-alpine
LABEL maintaner="Volkov Nikolai"
WORKDIR .
RUN apk add --no-cache zlib-dev jpeg-dev gcc musl-dev linux-headers libffi-dev build-base
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3", "run.py"]
HEALTHCHECK --interval=5s \
            --timeout=5s \
            CMD curl -f http://127.0.0.1:8000 || exit 1
