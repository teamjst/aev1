from django.shortcuts import render
from yeelight import Bulb, discover_bulbs
from .models import Settings
import threading
import queue

# Create your views here.


def adddevice_view(request):
    # Multi-threaded so it doesnt take forever to load page
    bulbqueue = queue.Queue()

    def queuewrap(queue):
        queue.put(discover_bulbs())
    discoverthread = threading.Thread(target=queuewrap, args=(bulbqueue,))
    discoverthread.start()
    # Sets up the IP list
    queryset = Settings.objects.all()
    context = {
        "bulb_list": queryset
    }
    discoverthread.join()
    bulbs = bulbqueue.get()
    ip = request.GET.get('ip')
    if request.GET.get('connect'):
        bulb = Settings()
        bulb.ip = ip
        if not Settings.objects.filter(ip__contains=ip):
            for x in bulbs:
                if x['ip'] == ip:
                    bulb.save()
        print(Settings.objects.all())
    return render(request, 'adddevice/adddevice.html', context)
