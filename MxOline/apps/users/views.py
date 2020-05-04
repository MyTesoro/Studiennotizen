from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from apps.users.form import *
from django.contrib.auth import authenticate, login
from django.urls import reverse


# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/login.html')

    def post(self, request, *args, **kwargs):
        # 实例化
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 用于通过用户名密码查询用户是否存在
            user_name = login_form.cleaned_data["username"]
            pass_word = login_form.cleaned_data["password"]
            user = authenticate(username=user_name, password=pass_word)
            # 判断user对象师傅存在
            if user is not None:
                # 不为空证明成功匹配到了用户
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                # return redirect("/login", {"msg": "用户名密码错误", "login_form": login_form})
                return render(request, "users/login.html", {"msg": "用户名密码错误", "login_form": login_form})
        else:
            # return redirect("/login", {"login_form": login_form})
            return render(request, "users/login.html", {"login_form": login_form})
