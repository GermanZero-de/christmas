FROM python:3.7-slim-buster


RUN apt-get update -y \
    && apt-get install -y gcc \
    && apt-get clean \
    && pip install pipenv

RUN adduser --gecos '' --disabled-password -u 1001 christmas
USER christmas
WORKDIR /home/christmas

ADD --chown=christmas:christmas . ./

RUN pipenv install

EXPOSE 8000

ENTRYPOINT pipenv run python main.py
