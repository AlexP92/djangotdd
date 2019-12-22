from django.http import HttpResponse
from django.shortcuts import  render

def home_page(request):
    context={'text':"Home"}
    return render(request,'home.html',context)

def about_page(request):
    context={'text':"About"}
    return render(request,'about.html',context)

def contact_page(request):
    context={'text':"Contact"}
    return render(request,'contact.html',context)