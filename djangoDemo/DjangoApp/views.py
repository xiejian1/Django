from django.shortcuts import render, render_to_response

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
# 表单
def search_form(request):
    return render_to_response('search_form.html')
# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        if request.POST['q']:
            ctx['rlt'] = request.POST['q']
        else:
            ctx['rlt'] = '输入的数据为空！请重新输入'
    return render(request, "post.html", ctx)

