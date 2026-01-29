from django.http import HttpResponse
from django.shortcuts import render
import requests

def index(request):
    return HttpResponse("<h1>Welcome to BlogPage</h1><p>This is the blog homepage.</p>")

def task_list(request):
    url = "https://naas.isalman.dev/no"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

    except requests.RequestException as e:
        return HttpResponse(f"Error fetching data: {e}", status=500)

    ctx={
        "tasks": [
            "task 1",
            "task 2",
            "task 3",
            "task 4"
        ],
        "data": data
    }

    return render(request, "task_list.html", ctx)   