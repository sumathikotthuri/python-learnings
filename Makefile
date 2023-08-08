install:
	#install commends
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#formatcode	
lint:
	#linting tools
test:
	#test
deploy:
	#deploy

all: install lint test deploy	