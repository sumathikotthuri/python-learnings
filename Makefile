install:
	#install commends
	pip install --upgrade pip &&\
		pip install -r requirements.txt
post-install:
	pre-commit install
lint:
	#linting tools
test:
	#test
	python -m pytest -vv --cov=projectlib testlib/*.py
build:
	#build container
	docker build -t deploy-fastapi .
run:
	#run docker
	docker run -p 127.0.0.1:8080:8080 f363ae6c84fe
deploy:
	#deploy

all: install post-install lint test build run deploy
