# Templates

## Template Structure Options

### App-Level Templates
```
appname/
└── templates/
    └── appname/
        └── index.html
```

### Project-Level Templates
```
project/
├── manage.py
├── templates/
│   └── base.html
└── appname/
```

## Configure Project-Level Templates
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

## Template Syntax

### Variables
```django
{{ variable }}
{{ name }}
```

### Tags
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

### Filters
```django
{{ my_date|date:"Y-m-d" }}
```

### Comments
```django
{# Single line comment #}

{% comment %}
Multi-line
comment
{% endcomment %}
```

## Basic Template
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
