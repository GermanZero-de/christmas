.PHONY: install test docker-build clean run

install:
	@echo "please install python 3 and pipenv"
	pipenv --python 3
	pipenv install

dev-install:
	@echo "please install python 3 and pipenv"
	pipenv --python 3
	pipenv install --dev

test:
	#pipenv check
	#pipenv run pytest --junit-xml=xunit-report.xml
	#pipenv run pytest --cov=christmas --cov-report=xml
	#pipenv run flake8
	pipenv run pytest

build:
	pipenv run pyinstaller main.py --name christmas --onefile

docker-build:
	docker build -t christmas:local .

clean:
	pipenv --rm
	rm -rf __pycache__/ build/ dist/ .pytest_cache/ .scannerwork/ christmas.egg-info/ xunit-report.xml .coverage coverage.xml

run:
	LOG_LEVEL=DEBUG pipenv run python main.py
