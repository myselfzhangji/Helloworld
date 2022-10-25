# HTML表单是网站交互性的经典方式, 本章将介绍如何用Django对用户提交的表单数据进行处理。 
from django.http import HttpResponse
from django.shortcuts import render

# 表单
def search_form(request):
    return render(request, 'search_form.html')

# 接受请求数据，GET方法
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q'] :
        message = '你搜索的内容: ' + request.GET['q']
    else :
        message = '你提交了空表单'

    return HttpResponse(message)