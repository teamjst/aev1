from django.shortcuts import render
from yeelight import Bulb, discover_bulbs
from .models import Settings
import threading
import queue

# Create your views here.


def adddevice_view(request):
    bulbqueue = queue.Queue()
    ip = request.GET.get('ip')
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

    # If user is found
    if Settings.objects.filter(username__exact=request.user.username):
        # Set bulb to be an object found in settings db
        bulb = Settings.objects.filter(username__exact=request.user.username)
        # Update ip if valid
        if request.GET.get('connect'):
            if bulb != ip:
                for x in bulbs:
                    if x['ip'] == ip:
                        bulb.ip = ip
                        bulb.update()
    # If no user is found (new user)
    else:
        # Create new object to save to db
        bulb = Settings()
        # Save if ip matches the
        if request.GET.get('connect'):
            if bulb != ip:
                for x in bulbs:
                    if x['ip'] == ip:
                        bulb.ip = ip
                        bulb.username = request.user.username
                        bulb.save()

    # user found
    # if Settings.objects.filter(username__exact=request.user):
    #     bulb = Settings.objects.filter(username__exact=request.user).first()
    #     if request.GET.get('connect'):
    #         if bulb != ip:
    #             for x in bulbs:
    #                 if x['ip'] == ip:
    #                     bulb.ip = ip
    #                     bulb.update()
    # # new user
    # else:
    #     bulb = Settings.objects.create(name=request.user.username)
    #     if request.GET.get('connect'):
    #         if bulb != ip:
    #             for x in bulbs:
    #                 if x['ip'] == ip:
    #                     bulb.ip = ip
    #                     bulb.update()

    return render(request, 'adddevice/adddevice.html', context)
