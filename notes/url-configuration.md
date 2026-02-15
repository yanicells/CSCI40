# URL Configuration

## App-Level URLs
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

## Project-Level URLs
```python
# project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('<appname>/', include('<appname>.urls', namespace="<appname>")),
    path('admin/', admin.site.urls),
]
```
