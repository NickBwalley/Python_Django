from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return render(request, 'MiraclesApp/homepage.html')

def login(request):
    response = redirect('MiraclesApp/Login.html')
    return response