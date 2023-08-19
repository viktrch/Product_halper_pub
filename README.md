# Сайт Foodgram, «Продуктовый помощник»


## Описание
Онлайн-сервис и API для сайта Foodgram, «Продуктовый помощник».
На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Версия
1.0.0

### Основные технологии
+ Python 3.10.6
+ Django 3.2
+ djangorestframework 3.14.0
+ djoser 2.2.0
+ django-filter 23.2
+ gunicorn
+ nginx
+ docker
+ github action
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение:
```
python3 -m venv env
```

```
source env/bin/activate
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
- Выполнить миграции:

```
python manage.py migrate
```
- В папке с файлом manage.py выполните команду:
```
python manage.py runserver
```
### Деплой проекта на удаленный сервер

- Для создания докер-образов сформируйте файл Dockerfile
- Сформируйте файл docker-compose.yml с вашими настройками
- В папке .github/workflows создайте файл main.yml с настройками github action
- Поместите "секреты" в .env
- скопируйте файлыdocker-compose.yml, .env на удаленный сервер
```
ssh -i путь_до_файла_с_SSH_ключом/название_файла_с_SSH_ключом имя_пользователя@ip_адрес_сервера
```
- отправьте ваш код в репозиторий github:
```
git push
```
- Запустите workflow с кнопки.
- Зайдите на удаленный сервер и выполните следующие команды:
```
docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/
```
- Выполните миграции в контейнере backend:
```
docker compose -f docker-compose.production.yml exec backend python manage.py migrate
```

### Авторы
Artem
