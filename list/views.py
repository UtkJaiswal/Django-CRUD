from django.http import HttpResponse
from django.shortcuts import render
from list.models import Tasks

def index(request):
    all_tasks = Tasks.objects.all()
    context = {
        'all_tasks':all_tasks
    }
    return render(request,"index.html",context)


def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        task = Tasks(title=title, desc=desc)
        task.save()
        all_tasks = Tasks.objects.all()
        context = {
            'all_tasks':all_tasks
        }
        
        return render(request,"index.html",context)
    return render(request,"create.html")