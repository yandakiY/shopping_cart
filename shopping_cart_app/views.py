from django.shortcuts import render, HttpResponse
from django.views import generic

# Create your views here.

# class Index(generic.ListView):
#     template_name = ""
#     context_object_name = ""
    
#     return 


def Index(request):
    return HttpResponse("Index page")