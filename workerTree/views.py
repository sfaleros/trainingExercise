from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse , request, HttpResponseRedirect
from django.shortcuts import render , redirect
# Create your views here.

class home(TemplateView):
    def get(self, request):


        from .models import Workers
        import random


        maxSalary= 10000000 
        firstnames = ['andre', 'vasyliy', 'ulia', 'elen', 'viktor', 'bob']
        lastnames=['brown', 'kostner', 'kaler', 'white', 'grey', 'amber'] 

        lastPeopleRang = 1
        lastPeople

        # Create your tests here.
        for i in range(50000):
            name = random.choice(firstnames) +" "+ random.choice(lastnames)
            salary=maxSalary - 200*i 
            boss =Workers.objects.latest('id')
            newWorker = Workers(full_name=name,salary= salary , boss = boss)
            newWorker.save()
            print(name)
            lastPeopleRang -=1
            if lastPeopleRang== 0 :
                lastpeople +=1 




        return  HttpResponse("<h1> hello </h1>")

