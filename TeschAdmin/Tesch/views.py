from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    context={}
    return render(request,'Tesch/login.html',context)

def home(request):
    #user = authenticate(username = 'nps_admin',password ='nps@123')
    #if user is not None:
        return HttpResponse("This is a home page")