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

def edit(request,id):
    curr_task = Tasks.objects.get(id=id)
    context = {
            'curr_task':curr_task
        }
    return render(request,"edit.html",context)

def save(request,id):
    curr_task_title = request.POST.get("title")
    curr_task_desc = request.POST.get("desc")

    curr_task=Tasks.objects.get(id=id)

    curr_task.title=curr_task_title
    curr_task.desc=curr_task_desc

    curr_task.save()

    all_tasks = Tasks.objects.all()

    context = {
            'all_tasks':all_tasks
        }
    
    return render(request,"index.html",context)

def delete(request,id):
    

    curr_task=Tasks.objects.get(id=id)


    curr_task.delete()

    all_tasks = Tasks.objects.all()

    context = {
            'all_tasks':all_tasks
        }
    
    return render(request,"index.html",context)