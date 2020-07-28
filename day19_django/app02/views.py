# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect


# Create your views here.

# USER_DICT = {
#     '1': {'name':'root','email':'aaa@123.com'},
#     '2': {'name':'root1','email':'aaa@123.com'},
#     '3': {'name':'root2','email':'aaa@123.com'},
#     '4': {'name':'root3','email':'aaa@123.com'},
#     '5': {'name':'root4','email':'aaa@123.com'}
# }

# def detail(request):
#从index.html 里传来的nid
#     # # nid = request.GET.get('nid')
#     # detail_info = USER_DICT[nid]
#     # return render(request, 'detail.html', {'detail_info': detail_info})


# def detail(request, uid, nid):
#     #urls.py传递的nid参数，添加nid参数
#     #动态传递参数，url匹配几个就得有参数，例如：(request, nid，uid)
#     #return HttpResponse(nid)
#     detail_info = USER_DICT[nid]
#     return render(request, 'detail.html', {'detail_info': detail_info})


# def index(request):
#     return render(request, 'index.html', {'user_dict':USER_DICT} )

def index(request):
    return render(request, 'index.html')

def user_info(request):
    user_list = models.UserInfo.objects.all()
    # print(user_list.query)#查看执行语句
    return render(request, 'user_info.html', {'user_list': user_list})

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
'''
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
        
'''


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        #数据库中执行select * from user where username='x' and password='x'

        u = request.POST.get('user')
        p = request.POST.get('pwd')

        obj = models.UserInfo.objects.filter(username=u,password=p).first()
        if obj:
            return redirect('/cmdb/index/')
        else:
            return render(request, 'login.html')

        return render(request, 'login.html')
    else:
        return redirect('/index/')



#=========================================================================
#orm基本的增删改查
from app02 import models
def orm(request):
    # insert 增数据
    # models.UserInfo.objects.create(username='root',password='123456')
    #不同写法
    # obj = models.UserInfo(username='syf',password='123456')
    # obj.save()
    #不同写法
    # dic = {'username':'eric', 'password':'123456'}
    # models.UserInfo.objects.create(**dic)

    ######数据库增删改查########

    #select 查数据
    #result = models.UserInfo.objects.all()
    result = models.UserInfo.objects.filter(username='root',password='123456')
    #print result
    for row in result:
        print (row.id,row.username,row.password)

    #删除语句
    #models.UserInfo.objects.filter(id='4').delete()

    #更新语句
    models.UserInfo.objects.filter(id=5).update(password='aaaaaa')



    return HttpResponse('orm,yes')




from django.views import View

class home(View):

    # 调用父类中的dispatch
    # def dispatch(self, request, *args, **kwargs):
    #     return HttpResponse('ok')

    def get(self,request):
        print (request.method)
        return render(request, 'home.html')

    def post(self,request):
        print (request.method, 'post')
        return render(request, 'home.html')





#=======================================================
#主机管理练习
def business(request):
    #对象
    v = models.Business.objects.all()
    #QuerySet
    #[obj(id,caption,code),obj(id,caption,code),obj(id,caption,code)]

    v1 = models.Business.objects.all().values('id','caption')
    #字典

    v2 = models.Business.objects.all().values_list('id','caption')
    #元组
    return render(request, 'business.html', {'v': v,'v1': v1,'v2':v2})


def host(request):
    v = models.Host.objects.filter(nid__gt=0)
    for row in v:
        print(row.nid, row.hostname,row.ip,row.port,row.b_id,row.b.caption)

    return HttpResponse("host")
    #return render(request, 'host.html', {'v':v})