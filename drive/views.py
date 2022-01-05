from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import Drive
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate, login, logout
from django.contrib.auth.decorators import login_required
import os


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("files:homepage")
    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "login.html", context)


@login_required(login_url='files:login')
def my_files(request):
    drive = Drive.objects.filter(owner_id=request.user.id)
    files = []
    dl = []
    for file in drive:
        file_size = os.path.getsize(file.file.path)
        file_size = file_size/1000
        dl.append(file.file.url)
        files.append(file_size)

    ctx = {'files': dl,
           'size': sum(files)}
    return render(request, 'index.html', ctx)


def homepage(request):
    ctx = {'username': request.user.username}
    return render(request, 'home.html', ctx)


def logout_request(request):
    logout(request)
    return redirect('files:homepage')


