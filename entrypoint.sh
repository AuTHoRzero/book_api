#!/bin/bash
echo "Migrate database"
python3 /opt/Book-api/book_api/manage.py migrate

echo "Creating superuser"
python3 /opt/Book-api/book_api/manage.py createsuperuser --noinput

echo "Running server"
python3 /opt/Book-api/book_api/manage.py runserver $START_HOST