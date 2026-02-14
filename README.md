# Django Cheat Sheet

## Environment Setup

### Create Virtual Environment
```bash
# Linux/Mac
python3 -m venv myenv
source ./myenv/bin/activate

# Windows
py -m venv myenv
.\myenv\Scripts\activate
```

### Deactivate Environment
```bash
deactivate
```

### Install Django
```bash
pip install Django
pip install python-dotenv
```

## Project Setup

### Create Django Project
```bash
django-admin startproject mysite
```

### Project Structure
```
mysite/
├── manage.py
└── mysite/
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── __init__.py
```

## Environment Variables (.env)

### Install python-dotenv
```bash
pip install python-dotenv
```

### Create .env file
Create `.env` in the same directory as `manage.py`:
```
SECRET_KEY='your-secret-key-from-settings'
STATIC_ROOT='path/to/static/folder'
```

### Update settings.py
```python
# settings.py - Add at top
from dotenv import load_dotenv
import os

load_dotenv()

# Update these settings
SECRET_KEY = os.getenv('SECRET_KEY')
STATIC_ROOT = os.getenv('STATIC_ROOT')
```

## Create Django App

```bash
python manage.py startapp <appname>
```

### Add App to INSTALLED_APPS
```python
# settings.py
INSTALLED_APPS = [
    ...,
    '<appname>',
]
```

## Views

### Function-Based View
```python
# appname/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World!')

def task_list(request):
    ctx = {
        "tasks": ["task 1", "task 2", "task 3"]
    }
    return render(request, "tasks/task_list.html", ctx)
```

### render() Function
Takes 3 arguments:
- `request` object
- Template name as string
- Context dictionary (optional)

## URL Configuration

### App-Level URLs
Create `urls.py` in your app folder:
```python
# appname/urls.py
from django.urls import path
from .views import index, task_list

app_name = "<appname>"

urlpatterns = [
    path('', index, name='index'),
    path('list', task_list, name='task-list'),
]
```

### Project-Level URLs
```python
# project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('<appname>/', include('<appname>.urls', namespace="<appname>")),
    path('admin/', admin.site.urls),
]
```

## Templates

### Template Structure Options

#### App-Level Templates
```
appname/
└── templates/
    └── appname/
        └── index.html
```

#### Project-Level Templates
```
project/
├── manage.py
├── templates/
│   └── base.html
└── appname/
```

### Configure Project-Level Templates
```python
# settings.py
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
```

### Template Syntax

#### Variables
```django
{{ variable }}
{{ name }}
```

#### Tags
```django
{% for item in items %}
    {{ item }}
{% endfor %}

{% if condition %}
    // Do something
{% elif other_condition %}
    // Do something else
{% else %}
    // Default
{% endif %}
```

#### Filters
```django
{{ my_date|date:"Y-m-d" }}
```

#### Comments
```django
{# Single line comment #}

{% comment %}
Multi-line
comment
{% endcomment %}
```

### Basic Template
```html
<!-- tasks/templates/tasks/task_list.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Task List</title>
</head>
<body>
    <ul>
      {% for task in tasks %}
        <li>{{ task }}</li>
      {% endfor %}
    </ul>
</body>
</html>
```

## Template Inheritance

### Base Template
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css">
    <title>{% block title %}My Site{% endblock %}</title>
    {% block styles %}{% endblock %}
</head>
<body>
    <div id="content">
        {% block content %}{% endblock %}
    </div>
    {% block scripts %}{% endblock %}
</body>
</html>
```

### Child Template
```html
<!-- tasks/templates/tasks/task_list.html -->
{% extends 'base.html' %}
{% load static %}

{% block title %}Task List{% endblock %}

{% block content %}
    <ul>
      {% for task in tasks %}
        <li>{{ task }}</li>
      {% endfor %}
    </ul>
{% endblock %}
```

### Using Child Template in View
```python
# tasks/views.py
def task_list(request):
    ctx = {"tasks": ["task 1", "task 2"]}
    return render(request, 'tasks/task_list.html', ctx)
```

## Static Files

### Setup Static Folder
Create `static/` folder in project root (sibling to `manage.py`)

### Configure settings.py
```python
# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = [os.path.join(BASE_DIR, 'static')]
```

### Use Static Files in Template
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<img src="{% static 'images/logo.png' %}">
```

## Run Server

```bash
python manage.py runserver
```

Access at: `localhost:8000`
