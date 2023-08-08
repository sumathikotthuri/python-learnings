install:
	#install commends
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	#linting tools
test:
	#test
	python -m pytest -vv --cov=projectlib testlib/*.py
build:
	#build container
deploy:
	#deploy

all: install lint test bbuild deploy
