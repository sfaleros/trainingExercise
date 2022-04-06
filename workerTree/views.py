from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse , request, HttpResponseRedirect
from django.shortcuts import render , redirect

# Create your views here.

class home(TemplateView):
    def get(self, request):


        from .models import Workers
        import random

        Workers =Workers.objects.all()



        '''
        gens=  16
        maxSalary= 10000000 
        firstnames = ['andre', 'vasyliy', 'ulia', 'elen', 'viktor', 'bob','ker', 'kit', 'max', 'alan', 'rose', 'lupa']
        lastnames=['brown', 'kostner', 'kaler', 'white', 'grey', 'amber','black', 'farer', 'li', 'lu', 'tur', 'tot'] 

        lastGenWorkers1 =[]
        lastGenWorkers=[Workers.objects.latest('id')]

        lastPeopleRang = 1
        #lastPeople

        # Create your tests here.
        for i in range(16):

            if i ==15:
                print("fuck")

            for a in lastGenWorkers:
                

                
                name = random.choice(firstnames) +" "+ random.choice(lastnames)
                salary=maxSalary - 200*i 
                #boss =Workers.objects.latest('id')
                newWorker = Workers(full_name=name,salary= salary , boss = a)
                newWorker.save()
                lastGenWorkers1.append(newWorker)
                print(name)

                name = random.choice(firstnames) +" "+ random.choice(lastnames)
                #boss =Workers.objects.latest('id')
                newWorker = Workers(full_name=name,salary= salary , boss = a)
                newWorker.save()
                lastGenWorkers1.append(newWorker)
                print("fffffffffffffffffffffff")
                print(name)

            lastGenWorkers=lastGenWorkers1
            lastGenWorkers1 =[]

            #name = random.choice(firstnames) +" "+ random.choice(lastnames)
            #salary=maxSalary - 200*i 
            #boss =Workers.objects.latest('id')
            #newWorker = Workers(full_name=name,salary= salary , boss = boss)
            #newWorker.save()
            #print(name)
            #lastPeopleRang -=1
            #if lastPeopleRang== 0 :
            #    lastpeople +=1 
        '''
        return render(request , 'workerTree/1.html',{Workers:Workers} )
        #return  HttpResponse(, {Workers=Workers})

