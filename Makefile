.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | \
	sort | \
	awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

build: ## Build
	docker build -t scrapli-course .
test: ## Run test
	docker run -v $(shell pwd):/source -w /local scrapli-course:latest pytest tests/ -vvv
