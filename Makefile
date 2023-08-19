install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

fmt:
	black .
	isort . --profile black

run:
	uvicorn src.server:app --port 8000 --reload

.PHONY: tests
tests:
	pytest . -vvs --showlocals