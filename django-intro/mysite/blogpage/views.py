from django.http import HttpResponse
from django.shortcuts import render
import requests

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

    url = "https://api.kanye.rest/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        kanye_data = response.json()
        data['kanye_quote'] = kanye_data

    except requests.RequestException as e:
        return HttpResponse(f"Error fetching Kanye quote: {e}", status=500)
    
    url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        insult_data = response.json()
        data['insult'] = insult_data
    except requests.RequestException as e:
        return HttpResponse(f"Error fetching insult: {e}", status=500)

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
        "tasks": [
            "task 1",
            "task 2",
            "task 3",
            "task 4"
        ],
        "data": data,
        "slug": task_slug
    }

    return render(request, "blogpage/task_list.html", ctx)   