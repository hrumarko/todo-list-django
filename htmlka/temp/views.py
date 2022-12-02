from django.shortcuts import render, redirect
from .forms import TaskForm, RegisterUserForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from .models import Task
from django.contrib.auth import logout


def index(request):
    if request.method == 'POST' and 'finish' in request.POST:
        id = request.POST.get('id')
        delete_task = Task.objects.filter(pk=id)
        delete_task.update(is_finished=True)
    if request.method == 'POST' and 'create' in request.POST:
        form = TaskForm(request.POST)
        if not form.is_valid():
            pass
        else:
            task = request.POST.get('task')
            description = request.POST.get('description')
            date = request.POST.get('date')
            user = request.user.id
            if date == '':
                Task.objects.create(task=task, description=description, user_id=user)
            else:
                Task.objects.create(task=task, description=description, date=date, user_id=user)
            form = TaskForm()
            tasks = Task.objects.filter(user=request.user.id, is_finished=False)
    else:
        form = TaskForm()
        tasks = Task.objects.filter(user=request.user.id, is_finished=False)

    ctx = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'index.html', ctx)


class UserRegister(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('login')


class UserLogin(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def account(request):
    tasks = Task.objects.filter(user=request.user.id, is_finished=True)
    all_tasks = Task.objects.filter(user=request.user.id).count()
    finish_tasks = Task.objects.filter(user=request.user.id, is_finished=True).count()
    ctx = {
        'tasks': tasks,
        'all_tasks': all_tasks,
        'finish_tasks': finish_tasks,
    }
    return render(request, 'account.html', ctx)
