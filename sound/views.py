from django.shortcuts import render

# Create your views here.
def sound_view(request):
    return render(request, 'sound/sound.html')
