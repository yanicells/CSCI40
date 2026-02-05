from django.views.generic import FormView
from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests

from .forms import TaskForm

tasks = []
form = TaskForm()

def index(request):
    return HttpResponse("<h1>Welcome to BlogPage</h1><p>This is the blog homepage.</p>")

def task_list(request, task_slug=None):
    url = "https://naas.isalman.dev/no"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

    except requests.RequestException as e:
        return HttpResponse(f"Error fetching data: {e}", status=500)

    url = "https://icanhazdadjoke.com/"
    try:
        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        joke_data = response.json()
        data['joke'] = joke_data
    except requests.RequestException as e:
        return HttpResponse(f"Error fetching joke: {e}", status=500)

    ctx={
        "tasks": tasks,
        "data": data,
    }

    return render(request, "blogpage/task_list.html", {**ctx, 'form': form, 'slug': task_slug or 'all'})   


class TaskAddView(FormView):
    template_name = 'blogpage/task_add.html'
    form_class = TaskForm
    success_url = '/blogpage/list/'

    def form_valid(self, form):
        tasks.append((form.cleaned_data['task_name'], form.cleaned_data['task_date']))
        return super().form_valid(form)