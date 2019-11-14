<h1>Сайт хуле</h1>

<h2>Хуле нет</h2>

Чтобы установить необходимые модули, выполните команду:
```pyhton
pip install -r requirements.txt
```

Для запуска:
```bash
cd newsite # переход в папку с сайтом

python manage.py makemigrations # назначить миграцию БД

python manage.py migrate # провести миграцию бд

python manage.py runserver # запустить сайт
```
