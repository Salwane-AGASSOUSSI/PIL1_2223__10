from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request,'login.html')
def Register(request):
    return render(request,'Register.html')

# Create your views here.
