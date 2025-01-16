from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

# def rahimah(req):
#     return HttpResponse("Hello, Rahimah!")
# def brian(req):
#     return HttpResponse("Hello, Brain!")

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")

def greet(request, name):
    return render(request, "hello/greet.html", {"name": name.capitalize()})

