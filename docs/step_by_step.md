LIST 
====

Step by step from :
docs/django_mfs_2012.pdf

$ virtualenv  Places_env
$ cd Places_env/ 
$ source bin/activate

# Install Django
$ pip install django
# Start new Project
$ django-admin.py startproject Places
$ cd Places 
$ chmod +x manage.py 
$ ./manage.py runserver


$ sensible-browser http://127.0.0.1:8000/ 
# Create Application
$ python manage.py startapp Places_app
$
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or
#Build the DB
$ python manage.py syncdb
 administrator: admin 
 password: admin 
 e-mail: jose.antonio.sa@gmail.com 
 
Edit models.py and so on ...
Edit views.py 
 


