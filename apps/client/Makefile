.PHONY: dev
dev: 
	@echo "Starting development server..."
	@bun run --watch index.ts

.PHONY: install
install:
	@echo "Installing dependencies..."
	@bun install

.PHONY: generate-client
generate-client:
	@echo "Generating client..."
	@bun run generate-client

.PHONY: test
test:
	@echo "Running tests..."
	@bun test

.PHONY: help
help:
	@echo "Available targets:"
	@echo "  dev            - Start the development server"
	@echo "  install        - Install dependencies"
