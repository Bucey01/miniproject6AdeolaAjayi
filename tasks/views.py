from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


def home(request):
    return render(request, 'tasks/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'tasks/register.html', {
        'form': form
    })


from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def dashboard(request):
    tasks = Task.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'tasks/dashboard.html', {
        'tasks': tasks
    })

from .forms import TaskForm


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False) 
            task.user = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'tasks/add_task.html', {
        'form': form
    })
