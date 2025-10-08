from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Tasks


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def tasks(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})


# def add_task(request):
#     return render(request, 'main/add_task.html')


def magic(request):
    return render(request, 'main/magic.html')
