from django.shortcuts import render

# Create your views here.
def lighttheme_list(request):
    return render(request, 'lightthemes/lighttheme_list.html')
