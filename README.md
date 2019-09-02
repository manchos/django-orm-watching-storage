django-orm-watching-storage
=====
Проект предназначен для автоматизации пульта охраны – онлайн-сервис по мониторингу визитов посетителей, 
просмотра истории посещений и информации по выданным пропускам.

Installing
----------

Create file .env in the root and write in it:

```
DB_HOST=db host
DB_PORT=db port
DB_NAME=db name
DB_USER=db user
DB_PASSWORD=password of db user
DEBUG=True or False to enable/disable debugging
SECRET_KEY=secret key
```
Python3 must be already installed.

```bash
pip install -r requirements.txt
```

How to use
----------------
To run local:

python manage.py runserver 0.0.0.0:8080

Адрес в браузере запущенного сайта –

**http://{ваш_localhost}:8080**

Project Goals
----------------

The code is written for educational purposes on online-course for web-developers
 [dvmn.org](https://dvmn.org/).
