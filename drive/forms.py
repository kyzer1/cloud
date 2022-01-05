from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.shortcuts import render
from .models import Drive
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate, login


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return REDIRECT_FIELD_NAME("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "login.html", context={"login_form":form})


def my_files(request):
    drive = Drive.objects.filter(owner_id=request.user.id)
    ctx = {'files': drive}
    return render(request, 'index.html', ctx)