from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello World")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("About Us")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("Contact Us")