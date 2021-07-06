from functools import reduce
from django.shortcuts import render
from .models import mymodel
from .forms import CreateNewUrl
from datetime import datetime
import random,string

def home(request):
    return render(request,'home.html')

def redirect(request,url):
    current_url = mymodel.objects.filter(new_url = url)
    if len(current_url) == 0:
        return render(request,'home.html')
    context = {'obj':current_url[0]}
    return render(request,'redirect.html',context)

def createUrl(request):
    if request.method == 'POST':
        form = CreateNewUrl(request.POST) #create new form
        if form.is_valid():
            real_website = form.cleaned_data['old_url']
            random_characters = list(string.ascii_letters)
            random_chars = ''
            for i in range(6):
                random_chars += random.choice(random_characters)
            while len(mymodel.objects.filter(new_url = random_chars))!=0:
                for i in range(6):
                    random_chars += random.choice(random_characters)
            
            d = datetime.now()
            s= mymodel(old_url = real_website,new_url = random_chars,time_created = d)
            s.save()
            return render(request,'urlcreated.html',{'chars':random_chars})
    
    else:
        form = CreateNewUrl()
        context = {'form':form}
        return render(request,'create.html',context)


