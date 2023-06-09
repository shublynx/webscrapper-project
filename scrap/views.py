from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from .models import Linkmodel

def index(request):

    if request.method == 'POST':
        site = request.POST.get('site','')
        page = requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')


        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Linkmodel.objects.create(address=link_address,name=link_text)
        return HttpResponseRedirect('/')
    else:

        data = Linkmodel.objects.all()

    return render(request,'scrap/index.html',{'data':data})

def delete(request):
    Linkmodel.objects.all().delete()
    return render(request,'scrap/index.html')

