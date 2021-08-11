.PHONY: tests

requirements.txt : requirements.in
	pip-compile -v

tests :
	pytest -v
