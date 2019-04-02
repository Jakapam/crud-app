#!/usr/bin/env bash
sleep 5
python manage.py db upgrade
sleep 1
python manage.py createadminuser
sleep 1
python manage.py mockdata
uwsgi --ini app.ini