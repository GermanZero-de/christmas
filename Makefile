.PHONY: install dev-install test docker-build clean run

install:
	@echo "please install python 3 and pipenv"
	pipenv --python 3
	pipenv install

dev-install:
	@echo "please install python 3 and pipenv"
	pipenv --python 3
	pipenv install --dev
	#pipenv run pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz

test:
	#pipenv check
	#pipenv run pytest --junit-xml=xunit-report.xml
	#pipenv run pytest --cov=christmas --cov-report=xml
	#pipenv run flake8
	pipenv run pytest

build:
	pipenv run pyinstaller main.py --name christmas --onefile --add-data data/postcodes.json:data/postcodes.json --add-data data/profile_data.json:data/profile_data.json

docker-build:
	docker build -t christmas:local .

docker-build-prod:
	docker build -t christmas:prod -f Dockerfile.prod .

clean:
	pipenv --rm
	rm -rf __pycache__/ build/ dist/ .pytest_cache/ .scannerwork/ christmas.egg-info/ xunit-report.xml .coverage coverage.xml christmas.spec

run:
	LOG_LEVEL=DEBUG pipenv run python main.py
