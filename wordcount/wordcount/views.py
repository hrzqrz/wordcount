from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello home')

def eggs(request):
    return HttpResponse('THis is eggs page')