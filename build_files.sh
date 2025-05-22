#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files for deployment
python manage.py collectstatic --noinput
