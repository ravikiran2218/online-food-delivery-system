#!/bin/bash

python manage.py migrate
python manage.py loaddata food_data.json || true
python manage.py collectstatic --noinput