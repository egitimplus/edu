from django.urls import path, include
from eduser.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('login/', EduLoginView.as_view(), name="account_login"),
    path('', include('allauth.urls')),
]

