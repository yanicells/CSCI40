from django.contrib import admin

from .models import Task, TaskGroup

class TaskGroupAdmin(admin.ModelAdmin):
    model = TaskGrou

class TaskAdmin(admin.ModelAdmin):
    model = Tasl


admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(Task, TaskAdmin)