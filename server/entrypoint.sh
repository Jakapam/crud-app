#!/usr/bin/env bash
python manage.py db upgrade
uwsgi --ini app.ini