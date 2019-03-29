from django.shortcuts import render
from yeelight import Bulb, discover_bulbs
from .models import Settings
import threading
import queue

# Create your views here.


def adddevice_view(request):
    bulbqueue = queue.Queue()
    ip = request.GET.get('ip')
    bulb = Settings.objects.filter(username__exact=request.user)
    queryset = Settings.objects.all()
    context = {
        "bulb_list": queryset
    }
    # Multi-threaded so it doesnt take forever to render
    def queuewrap(queue):
        queue.put(discover_bulbs())
    discoverthread = threading.Thread(target=queuewrap, args=(bulbqueue,))
    discoverthread.start()
    discoverthread.join()
    bulbs = bulbqueue.get()
    if request.GET.get('connect'):
        if bulb != ip:
            for x in bulbs:
                if x['ip'] == ip:
                    bulb.ip = ip
                    bulb.save()
    return render(request, 'adddevice/adddevice.html', context)
