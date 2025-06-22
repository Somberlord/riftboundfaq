# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.12-alpine AS builder

WORKDIR /src

COPY requirements.txt /src
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY .. /src

ENV FLASK_APP=riftboundfaq
ENTRYPOINT ["flask"]
CMD ["run"]

FROM builder as dev-envs