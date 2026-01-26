from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Welcome to BlogPage</h1><p>This is the blog homepage.</p>")

def task_list(request):
    ctx={
        "tasks": [
            "task 1",
            "task 2",
            "task 3",
            "task 4"
        ]
    }

    return render(request, "tasks/task_list.html", ctx)   