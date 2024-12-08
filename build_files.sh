#!/bin/bash

echo "BUILD START"

# Установить зависимости из Pipfile
pipenv install --deploy --ignore-pipfile

# Собрать статические файлы внутри окружения pipenv
pipenv run python manage.py collectstatic --noinput --clear

echo "BUILD END"
