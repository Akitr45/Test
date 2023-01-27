from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList,Item
# Create your views here.
def index(response, name):
    ls=ToDoList.objects.get(name=name)
    items=ls.objects.get(id=1)
    return HttpResponse ("%s"%(ls.name,str(items.text)))
