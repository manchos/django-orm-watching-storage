django-orm-watching-storage
=====
The project is designed to automate the security console-online service for monitoring visitors ' visits, 
view the history of visits and information on the issued passcards.

The security desk is a site that can be connected to the remote database with employees passcards and visits.

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

```bash
python manage.py runserver 0.0.0.0:8080
```

Open the page in the browser:

*http://{ваш_localhost}:8080*

Project Goals
----------------

The code is written for educational purposes on online-course for web-developers
 [dvmn.org](https://dvmn.org/).
