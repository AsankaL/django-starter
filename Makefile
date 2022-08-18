# find python3
PYTHON=.venv/bin/python

# our testing targets
.PHONY: tests flake black isort all format requirements

all: isort black flake tests
format: isort black flake

tests:
	${PYTHON} -m pytest tests

flake:
	${PYTHON} -m flake8 .

black:
	${PYTHON} -m black -t py38 .

isort:
	${PYTHON} -m isort --atomic .

requirements:
	poetry export -f requirements.txt -o requirements.txt --without-hashes
# end
