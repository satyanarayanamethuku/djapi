from django.shortcuts import render
from .models import Hyderabad

# Create your views here.

def index(request):
    return render(request,'index.html')


def hyderabad(request):
    form=Hyderabad.objects.all()
    return render(request,'hyd.html',{'form':form})