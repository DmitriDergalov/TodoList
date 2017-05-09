from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.filter().order_by('text')
    return render(request, 'todolist/todo_list.html', {'todos': todos})

def todo_new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todolist/todo_new.html', {'form': form})

def todo_del(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)	    
        todo.delete()
        return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todolist/todo_del.html', {})