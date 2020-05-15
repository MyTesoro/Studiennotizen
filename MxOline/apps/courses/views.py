from django.shortcuts import render
from django.views.generic import View
from apps.courses.models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from apps.operations.models import UserFavorite


# Create your views here.
class CoursesView(View):
    def get(self, request, *args, **kwargs):
        all_courses = Course.objects.all()

        sort = request.GET.get("sort", "")
        if sort:
            all_courses = Course.objects.order_by('-' + str(sort))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        advence_list = Course.objects.order_by('-students')[0:3]

        # per_page每页显示多少个
        p = Paginator(all_courses, per_page=5, request=request)
        courses = p.page(page)
        return render(request, 'courses/course-list.html',
                      {"all_courses": all_courses, "courses": courses, "sort": sort, "advence_list": advence_list})


class CourseDetailView(View):
    def get(self, request, course_id, *args, **kwargs):
        # 根据id查询课程
        course = Course.objects.get(id=int(course_id))
        # 点击到课程 的详情就记录一次点击数
        course.click_nums += 1
        course.save()
        # 获取收藏状态
        has_fav_course = False
        has_fav_org = False
        if request.user.is_authenticated:
            # 查询用户是否收藏了该课程和机构 fav_type=1证明是课程收藏，如果有，证明用户收藏了这个课
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=2):
                has_fav_org = True

        return render(request, 'courses/course-detail.html',
                      {"course": course, "has_fav_course": has_fav_course, "has_fav_org": has_fav_org})
