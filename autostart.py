import os
import sys

os.system("python manage.py makemigrations")
os.system("python manage.py migrate")
os.system("python manage.py createsuperuser")
os.system("python populatedb.py")
os.system("python generateTrafic.py 20")
os.system("python manage.py runserver")