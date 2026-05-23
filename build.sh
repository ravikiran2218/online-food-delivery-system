#!/usr/bin/env bash

python manage.py migrate
python manage.py loaddata food_data.json
python manage.py collectstatic --noinput