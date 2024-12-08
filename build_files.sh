#!/bin/bash

echo "BUILD START"

# Установить pipenv, если он не установлен
pip install pipenv

# Установить зависимости из Pipfile
pipenv install --deploy --ignore-pipfile

# Собрать статические файлы
pipenv run python manage.py collectstatic --noinput --clear

echo "BUILD END"
