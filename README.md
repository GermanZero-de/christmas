# GermanZero Weichnachtsaktion

## Install
### Development
`make dev-install`
### Production
`make install`
## Config
Environment Variables:
- `LOG_LEVEL` defaults to WARNING in Container and DEBUG with `make run`
- `PORT` defaults to 8000
## Run
`make run`
`PORT=8001 LOG_LEVEL=DEBUG make run`
## Docker-Build
`make docker-build`
or
`docker build -t christmas:local .`
