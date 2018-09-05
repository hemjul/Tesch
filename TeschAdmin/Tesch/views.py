from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    context={}
    return render(request,'Tesch/login.html',context)

def home(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username,password=password)
    if user is not None:
        return render(request,'Tesch/home.html',{})
    else:
        return render(request, 'Tesch/login.html', {
            'error_message': "Authentication failed.Invalid username/password",})
