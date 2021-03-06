from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import View

from apps.courses.models import Course
from apps.operations.models import Banner, UserFavorite
from apps.organizations.models import CourseOrg, Teacher
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
        next = request.GET.get("next", '')
        banners = Banner.objects.all().order_by("index")[:4]
        return render(request, 'users/login.html', {"next": next, "banners": banners})

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
        return render(request, "users/register.html")

    def post(self, request, *args, **kwargs):
        pass


class UserCenterView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, *args, **kwargs):
        current_page = 'info'
        return render(request, "users/usercenter-info.html", {"current_page": current_page})

    def post(self, request, *args, **kwargs):
        pass


class UserfavCourseView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, *args, **kwargs):
        current_page = 'fav'
        current_page2 = 'fav_c'
        fav_courses = UserFavorite.objects.filter(user=request.user, fav_type=1)
        fav_course_list = []
        for fav_org in fav_courses:
            course = Course.objects.get(id=fav_org.fav_id)
            fav_course_list.append(course)
        return render(request, "operations/usercenter-fav-course.html",
                      {"current_page": current_page, "current_page2": current_page2,
                       "fav_course_list": fav_course_list})

    def post(self, request, *args, **kwargs):
        pass


class UserfavOrgView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, *args, **kwargs):
        current_page = 'fav'
        current_page2 = 'fav_o'
        fav_orgs = UserFavorite.objects.filter(user=request.user, fav_type=2)
        fav_org_list = []
        for fav_org in fav_orgs:
            org = CourseOrg.objects.get(id=fav_org.fav_id)
            fav_org_list.append(org)
        return render(request, "operations/usercenter-fav-org.html",
                      {"current_page": current_page, "current_page2": current_page2, "fav_org_list": fav_org_list})

    def post(self, request, *args, **kwargs):
        pass


class UserfavTeacherView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, *args, **kwargs):
        current_page = 'fav'
        current_page2 = 'fav_t'
        fav_teachers = UserFavorite.objects.filter(user=request.user, fav_type=3)
        fav_teacher_list = []
        for fav_teacher in fav_teachers:
            teacher = Teacher.objects.get(id=fav_teacher.fav_id)
            fav_teacher_list.append(teacher)
        return render(request, "operations/usercenter-fav-teacher.html",
                      {"current_page": current_page, "current_page2": current_page2,
                       "fav_teacher_list": fav_teacher_list})

    def post(self, request, *args, **kwargs):
        pass


class UserMsgView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, *args, **kwargs):
        current_page = 'msg'
        return render(request, "operations/usercenter-message.html", {"current_page": current_page})

    def post(self, request, *args, **kwargs):
        pass


class IndexView(View):
    def get(self, request, *args, **kwargs):
        banners = Banner.objects.all().order_by("index")
        courses = Course.objects.filter(is_banner=False)[:8]
        course_orgs = CourseOrg.objects.all()[:15]
        small_banners = Course.objects.filter(is_banner=True)[:4]
        return render(request, 'users/index.html', {"banners": banners, "courses": courses, "course_orgs": course_orgs,
                                                    "small_banners": small_banners})
