from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
def task_view(request, *args, **kwargs):
    tasks = Task.objects.all()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            form = TaskForm()

    else:
        form = TaskForm()

    context = {"form" : form, "tasks" : tasks, "counter" : range(3)}
    return render(request, "tasks/all_tasks.html", context )
def update_task_view(request, key):
    task = Task.objects.get(id = key)
    form = TaskForm(instance = task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            form = TaskForm()
            return redirect("task_view")
    return render(request, 'tasks/update_task.html', {"form" : form, "task" : task} )


def delete_task_view(request, key):
    task = Task.objects.get(id = key)
    if request.method == "POST":
        task.delete()
        return redirect("task_view")
    return render(request, 'tasks/delete_task.html', {"task" : task} )
