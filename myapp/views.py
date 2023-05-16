from django.shortcuts import render
from django.http import HttpResponse
from .models import Data

def home(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        x=Data.objects.create(name=name,password=password)
        x.save()
    return render(request,'myapp/home.html')

def display(request):
    x=Data.objects.all().values()
    return render(request,'myapp/display.html',{'data':x})