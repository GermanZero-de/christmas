.PHONY: install test docker-build clean run

install:
	@echo "please install python 3 and pipenv"
	pipenv --python 3
	pipenv install --dev
	pipenv run pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz

test:
	pipenv check
	pipenv run pytest --junit-xml=xunit-report.xml
	pipenv run pytest --cov=xmascard --cov-report=xml
	pipenv run flake8

build:
	pipenv run pyinstaller main.py --name xmascard --onefile

docker-build:
	docker build -t xmascard:local .

clean:
	pipenv --rm
	rm -rf __pycache__/ build/ dist/ .pytest_cache/ .scannerwork/ xmascard.egg-info/ xunit-report.xml .coverage coverage.xml

run:
	LOG_LEVEL=DEBUG pipenv run python main.py
