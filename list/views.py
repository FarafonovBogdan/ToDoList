from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def task(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'list/list.html',context = {'tasks':tasks, 'form':form})


def new_task(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance = task)
    if request.method == 'POST':
        form  = TaskForm(request.POST,instance = task)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'list/new_task.html',context = {'form':form})


def delete(request,pk):
    delete = Task.objects.get(id = pk)
    if request.method == 'POST':
        delete.delete()
        return redirect('/')
    return render(request,'list/delete.html',context = {'delete':delete})
