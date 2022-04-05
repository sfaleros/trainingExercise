from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse , request, HttpResponseRedirect
from django.shortcuts import render , redirect
# Create your views here.

class home(TemplateView):
    def get(self, request):
        return  HttpResponse("<h1> hello </h1>")

