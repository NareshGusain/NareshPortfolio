from django.shortcuts import render , HttpResponse, redirect
from django.contrib.auth.models import User

def home(request):
    return render(request , 'base/index.html')

def resume(request):
    return render(request, 'base/resume.html')
