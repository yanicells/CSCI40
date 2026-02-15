# Static Files

## Setup Static Folder
Create `static/` folder in project root (sibling to `manage.py`)

## Configure settings.py
```python
# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = [os.path.join(BASE_DIR, 'static')]
```

## Use Static Files in Template
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<img src="{% static 'images/logo.png' %}">
```
