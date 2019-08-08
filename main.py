import os

from django.core.management import execute_from_command_line

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

execute_from_command_line("manage.py runserver 192.168.56.10:8080".split())
