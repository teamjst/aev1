from django.shortcuts import render, redirect
from yeelight import Bulb
from yeelight import *

bulb = Bulb("192.168.0.10")

# Create your views here.
def lighttheme_list(request):
    return render(request, 'lightthemes/lighttheme_list.html')

def fire_theme(request):

    transitions = [
    TemperatureTransition(1700, duration=1000),
    SleepTransition(duration=1000),
    TemperatureTransition(6500, duration=1000)
    ]

    flow = Flow(
    count=2,
    action=Flow.actions.recover,
    transitions=transitions
    )

    bulb.start_flow(flow)

    return redirect('lightthemes:lighthome')
