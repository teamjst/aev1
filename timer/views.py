from django.shortcuts import render

# Create your views here.
def timer_view(request):
    return render(request, 'timer/timer.html')
