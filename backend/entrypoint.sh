#!/bin/bash

# wait for database management command
python manage.py wait_for_db

python manage.py migrate

python manage.py initadmin

python manage.py collectstatic --no-input

exec "$@"