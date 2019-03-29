from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from adddevice.models import Settings

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save new user in DB amd log in
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            newuser = Settings()
            newuser.username = username
            newuser.save()
            return redirect('accounts:userhome')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def user_homepage(request):
    username = request.user
    context = {
        "Uname": username
    }
    return render(request, 'accounts/userhome.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:userhome')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })
