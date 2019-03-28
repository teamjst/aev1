from django.shortcuts import render

# Create your views here.
def adddevice_view(request):
    return render(request, 'adddevice/adddevice.html')
