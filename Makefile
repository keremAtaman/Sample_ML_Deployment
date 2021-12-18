SHELL := /bin/bash
.EXPORT_ALL_VARIABLES:
include .env

.PHONY: install_requirements clean init test lint terraform_validate

install_requirements: requirements.txt
	@echo "Installing requirements"
	pip install -r requirements.txt  

clean:
	@echo "Cleaning"
	rm -rf ./sample_ml_deployment

init: clean
	@echo "Initializing"
	mkdir ./sample_ml_deployment

test:
	tox

lint:
	tox -e lint

terraform_validate:
	terraform validate