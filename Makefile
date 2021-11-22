.PHONY=publish
publish:
	poetry build
	poetry publish

.PHONY=test
test:
	poetry run mypy .
	poetry run pytest

.PH