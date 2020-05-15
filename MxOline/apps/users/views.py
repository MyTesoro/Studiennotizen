from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from apps.users.form import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.urls import reverse
from apps.users.models import UserProfile


# Create your views here.
class CustomAuth(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 输入username和mobile都能查询到用户
            user = UserProfile.objects.get(
                Q(username=username) | Q(mobile=username) | Q(nick_name=username) | Q(
                    email=username))
            if user.check_password(password):  # 校验密码
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/login.html')

    def post(self, request, *args, **kwargs):
        # 实例化
        login_form = LoginForm(request.POST)
        login_status = {"msg": "", "login_form": login_form}
        if login_form.is_valid():
            # 用于通过用户名密码查询用户是否存在
            user_name = login_form.cleaned_data["username"]
            pass_word = login_form.cleaned_data["password"]
            user = authenticate(username=user_name, password=pass_word)
            # 判断user对象师傅存在
            if user is not None:
                # 不为空证明成功匹配到了用户
                login(request, user)
                return HttpResponseRedirect(reverse('users:index'))
            else:
                login_status['msg'] = '用户名密码错误'
                return render(request, "users/login.html", login_status)
        else:
            # return redirect("/login", {"login_form": login_form})
            login_status['msg'] = '用户名不存在'
        return render(request, "users/login.html", login_status)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('users:index'))


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request,"users/register.html")

    def post(self, request, *args, **kwargs):
        pass

