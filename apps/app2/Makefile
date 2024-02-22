.PHONY: dev
dev: 
	@echo "Starting development server..."
	@poetry run uvicorn fastapi_app_demo.main:app --reload

.PHONE: debug
debug:
	@echo "Starting development server in debug mode..."
	@poetry run python fastapi_app_demo/main.py

.PHONY: install
install:
	@echo "Installing dependencies..."
	@poetry install --with test

.PHONY: test
test:
	@echo "Running tests..."
	@poetry run pytest

.PHONY: export-requirements
export-requirements:
	@echo "Exporting requirements..."
	@poetry export -f requirements.txt --output requirements.txt --without-hashes

.PHONY: help
help:
	@echo "Available targets:"
	@echo "  install-poetry - Install Poetry"
	@echo "  dev            - Start the development server"
	@echo "  install        - Install dependencies"
	@echo "  test           - Run tests"
