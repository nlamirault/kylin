# Copyright (C) 2017-2018 Nicolas Lamirault <nicolas.lamirault@gmail.com>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

APP = kylin

SHELL = /bin/bash

VERSION=$(shell \
        grep RELEASE kylin/version.py \
        |awk -F'=' '{ print $$2 }' \
        |sed -e "s/[' ]//g")

NO_COLOR=\033[0m
OK_COLOR=\033[32;01m
ERROR_COLOR=\033[31;01m
WARN_COLOR=\033[33;01m

MAKE_COLOR=\033[33;01m%-20s\033[0m

.PHONY: help
help:
	@echo -e "$(OK_COLOR)==== $(APP) [$(VERSION)] ====$(NO_COLOR)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(MAKE_COLOR) : %s\n", $$1, $$2}'


.PHONY: init
init: ## Initialize environment
	@echo -e "$(OK_COLOR)[$(APP)] Initialize environment$(NO_COLOR)"
	test -d venv || virtualenv --python=/usr/bin/python3 venv
	. venv/bin/activate && \
		pip3 install -r requirements.txt && \
		pip3 install -r requirements-dev.txt

.PHONY: test
test: ## Unit tests
	@echo -e "$(OK_COLOR)[$(APP)] Launch unit tests$(NO_COLOR)"
	. venv/bin/activate && \
		tox -r

.PHONY: coverage
coverage: ## Code coverage
	@echo -e "$(OK_COLOR)[$(APP)] Launch unit tests$(NO_COLOR)"
	. venv/bin/activate && \
		tox -r -ecoverage

.PHONY: pkg-install
pkg-install: ## Install package
	@echo -e "$(OK_COLOR)[$(APP)] Install package $(NO_COLOR)"
	. venv/bin/activate && \
		python setup.py install && \
		rm -f AUTHORS ChangeLog

.PHONY: pkg-test
pkg-test: ## Test the distribution
	@echo -e "$(OK_COLOR)[$(APP)] Make a test-build$(NO_COLOR)"
	. venv/bin/activate && \
		python setup.py test && \
		rm -f AUTHORS ChangeLog

.PHONY: dist
pkg-dist: ## Create the distribution
	@echo -e "$(OK_COLOR)[$(APP)] Create the distribution$(NO_COLOR)"
	. venv/bin/activate && \
		python setup.py sdist && \
		rm -f AUTHORS ChangeLog

.PHONY: pkg-publish-test
pkg-publish-test: ## Publish to Pypi Test
	@echo -e "$(OK_COLOR)[$(APP)] Publish to Pypi TEST$(NO_COLOR)"
	. venv/bin/activate && \
		twine upload -r test dist/${APP}-${VERSION}.tar.gz && \
		rm -f AUTHORS ChangeLog

PHONY: pkg-publish
pkg-publish: ## Publish to Pypi
	@echo -e "$(OK_COLOR)[$(APP)] Publish to Pypi(NO_COLOR)"
	. venv/bin/activate && \
		twine upload dist/${APP}-${VERSION}.tar.gz && \
		rm -f AUTHORS ChangeLog
