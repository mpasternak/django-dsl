.PHONY: clean-pyc clean-build docs help
.DEFAULT_GOAL := help

help:
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

clean: clean-build clean-pyc

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint: ## check style with ruff
	uv run ruff check django_dsl tests

format: ## format code with ruff
	uv run ruff format django_dsl tests

test: ## run tests quickly with the default Python
	uv run pytest

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	uv run coverage run --source django_dsl -m pytest
	uv run coverage report -m
	uv run coverage html
	open htmlcov/index.html

release: clean ## package and upload a release
	uv build
	uv publish

sdist: clean ## package
	uv build
	ls -l dist
