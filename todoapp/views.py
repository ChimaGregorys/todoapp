from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from todoapp.models import Task

# Create your views here.
def index(request):
    items = Task.objects.all()
    return render(request, "index.html", {'items' : items})

def add(request):
    if request.method == "POST":
        task_name = request.POST['task']
	new_task = Task()
	new_task.name = task_name
	new_task.completed = False
	new_task.save()
	return redirect('/')

def remove(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')



