PROJECT_NAME := $(shell basename $CURDIR)
VIRTUAL_ENV := $(CURDIR)/.venv
LOCAL_PYTHON := $(VIRTUAL_ENV)/bin/python3

define HELP
Manage $(PROJECT_NAME). Usage:

make run        - Run $(PROJECT_NAME).
make install    - Create virtual env, install dependencies, and run project.
make deploy     - Install and run script by running `make install` and `make run` in succession.
make update     - Update pip dependencies via Poetry and export output to requirements.txt.
make format     - Format code with Pythons `Black` library.
make lint       - Check code formatting with `flake8`.
make clean      - Remove cached files and lock files.

endef
export HELP


.PHONY: run install deploy update format lint clean help

all help:
	@echo "$$HELP"


env: $(VIRTUAL_ENV)


$(VIRTUAL_ENV):
	if [ ! -d $(VIRTUAL_ENV) ]; then \
		echo "Creating Python virtual env in \`${VIRTUAL_ENV}\`"; \
		python3 -m venv $(VIRTUAL_ENV) \
		source $(VIRTUAL_ENV)/bin/activate;
	else \
		source $(VIRTUAL_ENV)/bin/activate;
	fi


.PHONY: run
run: env
	$(LOCAL_PYTHON) -m gunicorn --config=gunicorn.conf.py


.PHONY: install
install: env
	$(LOCAL_PYTHON) -m pip install --upgrade pip setuptools wheel && \
	$(LOCAL_PYTHON) -m pip install -r requirements.txt && \
	echo Installed dependencies in \`${VIRTUAL_ENV}\`;


.PHONY: deploy
deploy:
	make install && \
	make run


.PHONY: update
update: env
	$(LOCAL_PYTHON) -m pip install --upgrade pip setuptools wheel && \
	poetry update && \
	poetry export -f requirements.txt --output requirements.txt --without-hashes && \
	echo Installed dependencies in \`${VIRTUAL_ENV}\`;


.PHONY: format
format: env
	isort --multi-line=3 . && \
	black .


.PHONY: lint
lint:
	flake8 . --count \
			--select=E9,F63,F7,F82 \
			--exclude .git,.github,__pycache__,.pytest_cache,.venv,logs,creds,.venv,docs,logs \
			--show-source \
			--statistics


.PHONY: clean
clean:
	find . -name '.coverage' -delete && \
	find . -name '*.pyc' -delete \
	find . -name '__pycache__' -delete \
	find . -name 'poetry.lock' -delete \
	find . -name '*.log' -delete \
	find . -name '.DS_Store' -delete \
	find . -wholename '**/*.pyc' -delete && \
	find . -wholename '**/*.html' -delete && \
	find . -type d -wholename '__pycache__' -exec rm -rf {} + && \
	find . -type d -wholename '.venv' -exec rm -rf {} + && \
	find . -type d -wholename '.pytest_cache' -exec rm -rf {} + && \
	find . -type d -wholename '**/.pytest_cache' -exec rm -rf {} + && \
	find . -type d -wholename '**/*.log' -exec rm -rf {} + && \
	find . -type d -wholename './.reports/*' -exec rm -rf {} + && \
	find . -type d -wholename '**/.webassets-cache' -exec rm -rf {};