from django.shortcuts import render
from adddevice.models import Settings
from yeelight import Bulb

# Create your views here.
def timer_view(request):
    print(request.GET.get('timer'))
    return render(request, 'timer/timer.html')
