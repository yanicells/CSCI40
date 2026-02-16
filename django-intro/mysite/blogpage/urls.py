from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.TaskListView.as_view(), name='task_list')
    path('list/<int:id>/detail', TaskDetailView.as_view(), name='task-detail')
    path('add/', views.TaskAddView.as_view(), name='task_add'),
]

app_name = 'blogpage'
