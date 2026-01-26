from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to BlogPage</h1><p>This is the blog homepage.</p>")
