from django.shortcuts import render
from resto.models import Foodcort
#from django.contrib.auth import authenticate, login
#from django.contrib.auth import logout
from django.views import generic

def index(request):
    queryset = Foodcort.objects.all()
    context ={
            "object_list" : queryset
    }
    return render(request, 'index.html',context)
