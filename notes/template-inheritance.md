# Template Inheritance

## Base Template
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

## Child Template
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

## Using Child Template in View
```python
# tasks/views.py
def task_list(request):
    ctx = {"tasks": ["task 1", "task 2"]}
    return render(request, 'tasks/task_list.html', ctx)
```
