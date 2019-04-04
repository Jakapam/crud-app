#!/usr/bin/env bash
# The following is only for convenience to load mock data
sleep 5
python manage.py dropall
python manage.py db upgrade
sleep 1
python manage.py createadminuser
sleep 1
python manage.py mockdata
# delete above for actual application
uwsgi --ini app.ini