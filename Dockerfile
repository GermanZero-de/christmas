FROM python:3.8-buster


RUN apt-get update -y \
    && apt-get install \
    && apt-get clean \
    && pip install pipenv

RUN adduser --gecos '' --disabled-password -u 1001 christmas
USER christmas
WORKDIR /home/christmas

ADD --chown=christmas:christmas . ./

RUN make install

EXPOSE 8000

ENTRYPOINT make run
