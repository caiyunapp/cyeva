.PHONY: help build fmt lint sync lock upgrade all test

export PYTHONPATH := $(shell pwd)
export UV_PYTHON_PREFERENCE=only-system

help:
	@echo "Available commands:"
	@echo "  build    - Build the project using uv"
	@echo "  fmt      - Format the code using ruff"
	@echo "  lint     - Lint the code using ruff"
	@echo "  sync     - Sync and compile the project using uv"
	@echo "  lock     - Lock dependencies using uv"
	@echo "  upgrade  - Upgrade dependencies using uv"
	@echo "  all      - Run lock, sync, fmt, lint, and test"

build:
	uv build --no-sources

fmt:
	uv run ruff check --select I --fix .
	uv run ruff format .

lint:
	uv run ruff check --fix .
	uv run ruff format --check .

sync:
	uv sync --compile --frozen

lock:
	uv lock

upgrade:
	uv lock --upgrade

all: lock sync
	make fmt
	make lint
	make test	

test: lint
	uv run pytest --cov=cyeva/ ./tests/functions ./tests/test_issues.py

bench: sync
	uv run pytest --benchmark-warmup=off --benchmark-warmup-iterations=10 --benchmark-min-rounds=2 --benchmark-json output.json tests/test_perf.py   

freeze-doc-requirements:
	cd docs;uv lock;uv export > requirements.txt
