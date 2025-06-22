# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.12-alpine AS builder

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

ENV FLASK_APP=riftboundfaq.py
ENTRYPOINT ["flask"]
CMD ["run"]

FROM builder as dev-envs