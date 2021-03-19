from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(requst):
    return render(requst,"ncr/index.html")

def Ahmed(requst):
    return HttpResponse("Hello, Ahmed M.said!")

def greet(requst, name):
    #return render(f"Hello, {name.capitalize()}!")
    return render(requst,"ncr/greet.html",{
        "name":name.capitalize()
    })
    