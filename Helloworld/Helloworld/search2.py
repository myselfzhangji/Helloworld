# -*- coding: utf-8 -*-

#提交数据时更常用 POST 方法。我们下面使用该方法，并用一个URL和处理函数，同时显示视图和处理请求。

from django.views.decorators import csrf
from django.shortcuts import render

# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']

    return render(request, "post.html", ctx)