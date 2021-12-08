from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def helloWorld(request):
    return HttpResponse("Hello World!")

def index(request):
    val = "Prashant Kumar Dey"
    return render(request, "index.html", {"name": val})