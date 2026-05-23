#!/bin/sh

pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata food_data.json
python manage.py collectstatic --noinput