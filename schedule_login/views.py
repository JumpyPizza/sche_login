from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
# Create your views here.


def index(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if request.POST['username']== '' or request.POST['password']=='' :
            return render(request, 'schedule_login/index.html', {'error_no_unps': '请输入用户名或密码'})
        elif user == None:
            return render(request,'schedule_login/index.html', {'error': '用户名/密码错误'})
        elif user.is_active:
            login(request, user)
            return redirect('/schedule/')
    else:
        return render(request, 'schedule_login/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/')

    else:
        form = UserCreationForm()
    return render(request, 'schedule_login/register.html',context={'form': form})

@login_required(login_url='/index/')
def schedule(request):
    return render(request, 'schedule_login/schedule.html')


def userLogout(request):
    logout(request)
    return redirect('/index/')


