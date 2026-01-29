from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.task_list, name='task_list_default'),
    path('list/<str:task_slug>/', views.task_list, name='task_list'),
]

app_name = 'blogpage'
