from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def task_list(request):
    return render(request, 'main/task_list.html')


def add_task(request):
    return render(request, 'main/add_task.html')


def magic(request):
    return render(request, 'main/magic.html')
