from django.http import HttpResponse
from django.shortcuts import render
from list.models import Tasks

def index(request):
    return render(request,"index.html")


def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        print("Title is ",title)
        
        task = Tasks(title=title, desc=desc)
        task.save()
        return render(request,"index.html")
    return render(request,"create.html")