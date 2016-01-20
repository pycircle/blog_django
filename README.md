# Blog Django

## Overview

Simple example of blog created in django with bower integration. UIkit used as frontent.

### Installation

Go to src directory:

```
cd src
```

Install requirements for pip and bower:

```
pip install -r requirements.txt && python manage.py bower install
```

Compile translations from .po files:

```
python manage.py compilemessages
```

Discover models and create database:

```
python manage.py makemigrations && python manage.py migrate
```

Create superuser:

```
python manage.py createsuperuser
```

Run project in localhost (only for development):

```
python manage.py runserver
```
