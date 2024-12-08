
echo "BUILD START"

# Установить зависимости из requirements.txt
python3.9 -m pip install -r requirements.txt

# Собрать статические файлы
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"