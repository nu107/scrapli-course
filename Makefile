.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | \
	sort | \
	awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

build: ## Build
	docker build -t scrapli-course . -f Dockerfile

cli: ## CLI
	docker run -it -v $(shell pwd):/local -w /local --env-file .env scrapli-course:latest bash

test: ## Test
	docker run -it -v $(shell pwd):/local -w /local --env-file .env scrapli-course:latest pytest tests/ -vvv

test-lf: ## Test last-failed
	docker run -it -v $(shell pwd):/local -w /local --env-file .env scrapli-course:latest pytest --lf tests/ -vvv
