from django.shortcuts import render

from django.http import HttpResponse 
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
#from django.views.generic.edit import DeleteView 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView  
from .models import GeeksModel
  
class MyView(View): 
    def get(self, request): 
        return HttpResponse('result') 
  
class GeeksCreate(CreateView): 
    model = GeeksModel   
    fields = ['title', 'description']
    success_url ="/"

class GeeksList(ListView):  
    model = GeeksModel

class GeeksDetailView(DetailView):  
    model = GeeksModel  
  
class GeeksUpdateView(UpdateView):  
    model = GeeksModel 
   
    fields = [ 
        "title", 
        "description"
    ] 
    success_url ="/"


class GeeksDeleteView(DeleteView): 
    model = GeeksModel 
    success_url ="/"
