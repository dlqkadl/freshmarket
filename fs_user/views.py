# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http.response import JsonResponse, HttpResponseRedirect
from models import UserInfo
from hashlib import sha1


def register(request):
    return render(request, 'fs_user/register.html')


def register_handle(request):
    # 接受用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    # 判断两次密码输入是否一致
    if upwd != upwd2:
        return redirect('/user/register/')

    # 密码加密
    sha = sha1()
    sha.update(upwd)
    upw3 = sha.hexdigest()

    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upw3
    user.uemail = uemail
    user.save()

    # 注册成功，转到登录页
    return redirect('/user/login/')


def register_exist(request):
    uname = request.Get.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {
        'title': '用户登录',
        'error_name_or_pwd': 0,
        'uname': uname
    }
    return render(request, 'fs_user/login.html', context)


def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    remember = post.get('remember', 0)

    users = UserInfo.objects.filter(uname=uname)
    content = {
        'title': '用户登录',
        'error_name_or_pwd': 0,
        'uname': uname,
        'upwd': upwd
    }
    if len(users) == 1:
        name = users[0].uname
        pwd = users[0].upwd

        sha = sha1()
        sha.update(upwd)
        if uname != name or pwd != sha.hexdigest():
            content['error_name_or_pwd'] = 1
            return render(request, 'fs_user/login.html', content)
        else:
            red = HttpResponseRedirect('/user/info/')
            if remember != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
    else:
        content['error_name_or_pwd'] = 1
        return render(request, 'fs_user/login.html', content)


def info(request):
    user = request.session['user_name']
    content = {
        'user': user
    }
    return render(request, 'fs_user/user_center_info.html', content)


def order(request):
    return render(request, 'fs_user/user_center_order.html')


def site(request):
    return render(request, 'fs_user/user_center_site.html')




