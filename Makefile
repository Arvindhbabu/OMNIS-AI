setup:
	uv sync

install:
	uv sync

lint:
	ruff check .

format:
	ruff format .

typecheck:
	mypy .

test:
	pytest

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache
