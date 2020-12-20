help: ## help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## install development requirements
	pip install -r requirements.txt

test: ## run tests
	pytest

test-cov: ## run tests with coverage
	pytest --cov kineticpy/
