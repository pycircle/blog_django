# Blog Django

## Overview

Simple example of blog created in django with bower integration. Semantic-UI used as frontent.

### Installation

Install requirements for pip and bower:

```
pip install -r requirements.txt && python manage.py bower install
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
