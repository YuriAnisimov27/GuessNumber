#!make
SHELL = /usr/bin/env bash

.PHONY: help prepare-dev run

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))

help:
	@echo "make prepare-dev"
	@echo "       prepare development environment, use only once"
	@echo "make venv"
	@echo "       create virtual environment for application"
	@echo "make run"
	@echo "       run project"

prepare-dev:
	sudo apt-get -y install python3.5 python3-pip
	python3 -m pip install virtualenv
	make venv

# Requirements are in setup.py, so whenever setup.py is changed, re-run installation of dependencies.
venv: 
	virtualenv -p python3 $(mkfile_dir)/dir_venv

	( \
		source $(mkfile_dir)/dir_venv/bin/activate; \
		export PIP_CONFIG_FILE=$(mkfile_dir)/pip.conf; \
		pip install -r $(mkfile_dir)/requirements.txt --no-deps \
	)

run:
	$(mkfile_dir)/dir_venv/bin/python3 FirstGame.py

clean-build:  ## remove build artifacts
	rm -fr $(mkfile_dir)/dir_venv/