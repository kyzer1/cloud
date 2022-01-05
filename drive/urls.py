from django.urls import path
from .models import Drive
from .views import login_request, homepage, logout_request
from .views import my_files

app_name = 'drive'

urlpatterns = [
    path('my-files/', my_files, name='my-files'),
    path("login/", login_request, name="login"),
    path("", homepage, name="homepage"),
    path('logout/', logout_request, name='logout')
]