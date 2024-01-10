#!/usr/bin/env bash
# exit on error
set -o errexit

export PATH="/opt/render/project/poetry/bin:$PATH"

poetry install --no-root

poetry run python manage.py collectstatic --no-input
poetry run python manage.py migrate