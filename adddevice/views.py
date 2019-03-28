from django.shortcuts import render
from yeelight import Bulb
from .models import Settings

# Create your views here.


def adddevice_view(request):
    #Sets up the IP list
    queryset = Settings.objects.all()
    context = {
        "bulb_list": queryset
    }
    ip = request.GET.get('ip')
    print(ip)
    if request.GET.get('connect'):
        bulb = Settings()
        bulb.ip = ip
        if not Settings.objects.filter(ip__contains=ip):
            bulb.save()
        print(Settings.objects.all())
    return render(request, 'adddevice/adddevice.html', context)
