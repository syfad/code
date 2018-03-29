# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect


# Create your views here.

def index(request):
    return HttpResponse('hello index')

# def login(request):
#     if request.method == "GET":
#         return render(request, 'login.html')
#     elif request.method == "POST":
#         u = request.POST.get('user')
#         p = request.POST.get('pwd')
#         if u == 'syf' and p == '123456':
#             return redirect('/index/')
#         else:
#             return redirect(request, 'login.html')
#     else:
#         return redirect('/index/')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":

        # 获取radio
        # v = request.POST.get('gender')
        # print v

        #获取CheckBox，多选择
        # v = request.POST.getlist('favor')
        # print v

        # 取文件上传的文件名
        # v = request.POST.get('fafafa')
        # print v

        #上传文件， html form标签需要加特殊设置：（enctype="multipart/form-data"）
        obj = request.FILES.get('fafafa')
        print obj, type(obj), obj.name

        #上传文件功能，文件上传至新建目录upload文件夹内。
        import os
        file_path = os.path.join('upload', obj.name)
        f = open(file_path, mode="wb")
        for i in obj.chunks():
            f.write(i)
        f.close()

        return render(request, 'login.html')


from django.views import View

class home(View):

    # 调用父类中的dispatch
    def dispatch(self, request, *args, **kwargs):
        return HttpResponse('ok')

    def get(self,request):
        print (request.method)
        return render(request, 'home.html')

    def post(self,request):
        print request.method, 'post'
        return render(request, 'home.html')









