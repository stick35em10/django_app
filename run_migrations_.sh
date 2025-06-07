#!/bin/bash

#!/usr/bin/env bash

# Exit on error
set -o errexit

echo "--- Installing Python dependencies ---"
pip install -r requirements.txt

echo "--- Collecting static files ---"
python manage.py collectstatic --no-input

echo "--- Applying database makemigrations ---"
python manage.py makemigrations

echo "--- Applying database migrations ---"
python manage.py migrate

echo "--- Build process completed successfully! ---"

# python3 manage.py migrate
