from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request): 
    
    return HttpResponse("Welcome to my book store.") 
def htmlfile(request):
    return render(request, "hello.html",{"name":"Abdulaziz"})