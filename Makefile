# USAGE: make <command>
# Example: make add_dev_reqs
# It will create a archive with all libs
.PHONY: install format lint test sec clean cover add_dev_reqs before_push_code

# Terminal Colors
Color_Off=\033[0m
Black=\033[1;30m
Red=\033[1;31m
Green=\033[1;32m
Yellow=\033[1;33m


install:
	@poetry update

format:
	@ruff format

lint:
	@ruff check src/

req:
	@pipreqs --force src/

doc:
	@docformatter --in-place --config setup.cfg src/**/*.py
	@pydocstyle --ignore=D100,E402,W293,D107,D413,D202,D212,D407,D406,D103,D104,D200,D412,D205,D400 src/
	
security:
	@pip-audit

clean:
	find . -type d -name __pycache__ -exec rm -r {} \+

run_app:
	uvicorn src.app.main:app --reload

before_push_code:
	${MAKE} clean
	${MAKE} format