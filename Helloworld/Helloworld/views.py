from django.shortcuts import render

'''
def runoob(request):
    import datetime
    now = datetime.datetime.now()
    name = 0
    return render(request, "runoob.html", {"time":now})
'''

'''
def runoob(request):
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    return render(request, "runoob.html", {"views_str":views_str})
'''

'''
def runoob(request):
    views_num = 88
    return render(request, "runoob.html", {"num":views_num})
'''

'''
def runoob(request):
    views_list = ["菜鸟教程","菜鸟教程1","菜鸟教程2","菜鸟教程3",]
    return render(request, "runoob.html", {"views_list":views_list})
'''

'''
def runoob(request):
    views_dict = {"name":"菜鸟教程","age":18}
    return render(request, "runoob.html", {"views_dict":views_dict})
'''

def runoob(request):
    name ="菜鸟教程"
    return render(request, "runoob.html", {"name": name})