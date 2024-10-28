# Makefile

VENV_DIR := .venv

.PHONY: venv clean format

venv:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt

clean:
	rm -rf $(VENV_DIR)

format:
	black . && isort .