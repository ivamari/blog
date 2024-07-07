# blog_test

Технологии
* Python
* Django REST Framework (DRF)
* PostgreSQL 

## Основной функционал
### Посты
* Просмотр списка постов
* Деталка поста
* Создание поста
* Обновление поста
* Удаление поста

## Как запустить проект:

### Клонировать репозиторий и перейти в него в командной строке:

`https://github.com/ivamari/blog_test.git`

`cd blog_test`

### Cоздать и активировать виртуальное окружение:

`python -m venv env`

`source venv/bin/activate`

### Установить зависимости из файла requirements.txt:

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

### Выполнить миграции:

`python manage.py migrate`

### Запустить проект:

`python manage.py runserver`

## Примеры запросов к API
Примеры запросов и JSON ответы можно посмотреть в документации после запуска проекта по адресу: http://127.0.0.1:8000/api/
