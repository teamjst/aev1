from django.urls import path
from . import views

app_name = 'sound'

urlpatterns = [
    path('', views.sound_view, name="soundhome"),
]
