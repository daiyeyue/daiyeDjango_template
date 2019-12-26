from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def one(request):
    return render(request, template_name='one.html')

def two(request):

    # 用字典来传递模板中需要的数据，ct代表上下文的缩写
    ct = dict()
    ct["name"] = "wangxiaojing"
    return render(request, template_name='two.html', context=ct)

def three(request):
    ct = dict()
    ct["score"] = [99,98,23,100]
    return render(request, template_name='three.html', context=ct)

def four(request):
    ct = dict()
    ct["name"] = '王晓静'
    return render(request, template_name='four.html', context=ct)

def five_get(request):
    return render(request, template_name='five_get.html')

def five_post(request):
    print(request.POST)
    return render(request, template_name='one.html')
