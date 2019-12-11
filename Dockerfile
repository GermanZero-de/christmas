FROM python:3.8-buster AS builder

ADD . ./

RUN apt-get update -y \
    && apt-get install -y python3-dev wget make unzip \
    && apt-get clean \
    && pip install pipenv \
    && make install \
    && make build

FROM python:3.8-slim

RUN adduser --gecos '' --disabled-password -u 1001 xmascard
USER xmascard
WORKDIR /home/xmascard

COPY --chown=xmascard:xmascard --from=builder dist/xmascard .

EXPOSE 8000

ENTRYPOINT ["./xmascard"]
