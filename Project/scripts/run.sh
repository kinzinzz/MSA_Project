#!/bin/sh
set -e

python manage.py migrate
gunicorn -b :8080 --chdir /admin admin.wsgi:application
