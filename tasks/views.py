from django.shortcuts import render

tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(req):
    return render(req, "tasks/index.html", {
        "tasks": tasks
    })
