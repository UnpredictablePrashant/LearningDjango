from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegistrationForm
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.

def helloWorld(request):
    return HttpResponse("Hello World!")

def index(request):
    val = "Prashant Kumar Dey"
    return render(request, "index.html", {"name": val})

def register(request):
    if request.method == "POST":
        f = CustomRegistrationForm(request.POST)
        if f.is_valid():
            f.save()
    else:
        f = CustomRegistrationForm()
    return render(request, 'register.html', {'form': f})

#This register was used when we were using the value from the auth.forms UserCreationForm
# def register(request):
#     if request.method == "POST":
#         f = UserCreationForm(request.POST)
#         print(f.is_valid())
#         if f.is_valid():
#             f.save()
#     else:
#         f = UserCreationForm()
#     return render(request, 'register.html', {'form': f})


# Please go through the documentation https://docs.djangoproject.com/en/3.2/topics/auth/default/
def signin(request):
    if request.method == "POST":
        f = AuthenticationForm(request=request, data=request.POST)
        if f.is_valid():
            un = f.cleaned_data['username']
            pd = f.cleaned_data['password']
            user = authenticate(username = un, password = pd)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile')
                # return render(request, 'profile.html')
    else:
        f = AuthenticationForm()
    return render(request, 'login.html', {'form': f})

def userProfile(request):
    return render(request, 'profile.html', {'name': request.user})

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/login')

