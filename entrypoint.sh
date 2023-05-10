#!/bin/sh -e

./manage.py migrate

exec gunicorn --bind=0.0.0.0:8000 config.wsgi
