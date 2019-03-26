from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup_view, name="signup"),
    path('userhome', views.user_homepage, name="userhome"),
    path('login', views.login_view, name="login"),
]
