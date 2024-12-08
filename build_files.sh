#!/bin/bash

echo "BUILD START"

# Установить зависимости из Pipfile
pipenv install --deploy --ignore-pipfile

# Активировать окружение pipenv
pipenv shell

# Собрать статические файлы
python manage.py collectstatic --noinput --clear

echo "BUILD END"
