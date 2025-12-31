# Makefile for Emotional Comprehension Pipeline

.PHONY: help install install-dev test lint format type-check clean build docs

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install package in production mode
	pip install -e .

install-dev:  ## Install package with development dependencies
	pip install -e ".[dev]"
	pre-commit install

test:  ## Run tests with coverage
	pytest --cov=emo_comprehension --cov-report=term-missing --cov-report=html

test-quick:  ## Run tests without coverage
	pytest -v

lint:  ## Run all linters
	flake8 src tests
	black --check src tests
	isort --check-only src tests

format:  ## Format code with black and isort
	black src tests
	isort src tests

type-check:  ## Run type checking with mypy
	mypy src

clean:  ## Clean build artifacts and cache files
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build:  ## Build distribution packages
	python -m build

docs:  ## Build documentation
	cd docs && make html

all: format lint type-check test  ## Run format, lint, type-check, and test

pre-commit:  ## Run pre-commit hooks on all files
	pre-commit run --all-files
