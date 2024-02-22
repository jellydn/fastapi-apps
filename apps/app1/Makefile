.PHONY: dev
dev: 
	@echo "Starting development server..."
	@uvicorn app.main:app --reload

.PHONE: debug
debug:
	@echo "Starting development server in debug mode..."
	@python3 app/main.py

.PHONY: install
install:
	pip install --no-cache-dir -r requirements.txt

.PHONY: install-dev
install-dev:
	pip install --no-cache-dir -r requirements-dev.txt

.PHONY: test
test:
	@echo "Running tests..."
	pytest
