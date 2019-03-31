#!/usr/bin/env bash
if [ $PERFORM_MIGRATIONS == "true" ]
then
    python manage.py db migrate
fi
python manage.py db upgrade
uwsgi --ini app.ini