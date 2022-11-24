from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'home.html', {'safa': 'This is me'})

def eggs(request):
    return HttpResponse('THis is eggs page')
