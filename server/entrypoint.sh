#!/usr/bin/env bash
python manage.py db upgrade
python manage.py createadminuser
python manage.py mockdata
uwsgi --ini app.ini