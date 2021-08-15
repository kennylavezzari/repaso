from django.shortcuts import render
from .models import auto,chofer
# Create your views here.

def autoview(request):
    objetos= auto.objects.all()
    return render(request,'auto.html',{'valores':objetos})

def choferview(request):
    objetos= chofer.objects.all()
    return render(request,'chofer.html',{'valores':objetos})
