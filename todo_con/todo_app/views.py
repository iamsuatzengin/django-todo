from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm
# Create your views here.

login_required(login_url='login')
def index(request):
    tasks = Todo.objects.filter(created_by=request.user).order_by('-created_at')
    form = TodoForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.created_by = request.user
        task.save()
        messages.success(request, 'Görev Başarıyla Eklendi!')
        return redirect('index')
    return render(request, 'index.html', {'tasks': tasks, 'form': form})

login_required(login_url='login')
def update(request, id):
    task = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        task = form.save(commit=False)
        task.created_by = request.user
        task.save()
        messages.success(request, 'Görev Başarıyla Güncellendi!')
        return redirect('index')
    return render(request, 'update.html', {'task': task, 'form': form})

login_required(login_url='login')
def delete(request, id):
    task = Todo.objects.get(id=id)
    task.delete()
    messages.info(request, 'Silme işlemi başarılı!')
    return HttpResponseRedirect('/index')

login_required(login_url='login')
def deleteAll(request):
    tasks = Todo.objects.all()
    tasks.delete()
    messages.info(request, 'Hepsi silindi!')
    return HttpResponseRedirect('/index')
