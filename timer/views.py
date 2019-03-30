from django.shortcuts import render
from adddevice.models import Settings
from yeelight import Bulb
import datetime
import threading


# Create your views here.
def timer_view(request):
    userbulb = Settings.objects.filter(username__exact=request.user)
    startpause = False
    bulb = Bulb(userbulb[0].ip)
    if request.GET.get('timerstart'):
        timeone = request.GET.get('timepicker-one')
        timetwo = request.GET.get('timepicker-two')

        def delZero(time):
            intver = int(time[0])
            if intver < 10:
                return "0" + time
            else:
                return time
        timeone = delZero(timeone)
        timetwo = delZero(timetwo)
        while timetwo != datetime.datetime.now().strftime("%I : %M %p"):
            if timeone == datetime.datetime.now().strftime("%I : %M %p") and startpause is False:
                bulb.turn_on()
                startpause = True
        bulb.turn_off()
    return render(request, 'timer/timer.html')

