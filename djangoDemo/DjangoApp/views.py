from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.views.generic.base import View

from DjangoApp.models import User
from DjangoApp.dbtest import find
def hello1(request):
    return HttpResponse("Hello world ! ")
def index(request):
    return HttpResponse("hello smallqiang!")
def hello(request):
    user = User.objects.get(id=4)
    contenx = {}
    contenx['hello'] = user.name
    return render(request,'hello.html',contenx)
class IndexView(View):
     def get(self,request):
        user =  User.objects.get(id=4)
        return render(request,'hello.html',{"hello":user.name})

