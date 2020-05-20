from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View
from apps.operations.form import *
from django.http import JsonResponse
from apps.operations.models import *
from apps.courses.models import Course
from apps.organizations.models import CourseOrg
from apps.organizations.models import Teacher


class AddFavView(View):
    # 先判断用户是否登录
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"status": "fail", "msg": "用户未登录"})
        use_fav_form = UserFavForm(request.POST)
        if use_fav_form.is_valid():
            fav_id = use_fav_form.cleaned_data["fav_id"]
            fav_type = use_fav_form.cleaned_data["fav_type"]
            # 判断用户是否已经收藏
            existed_records = UserFavorite.objects.filter(user=request.user, fav_id=fav_id, fav_type=fav_type)
            if existed_records:
                # 收藏这条信息删除
                existed_records.delete()
                if fav_type == 1:
                    course = Course.objects.get(id=fav_id)
                    course.fav_nums -= 1
                    course.save()
                elif fav_type == 2:
                    course_org = CourseOrg.objects.get(id=fav_id)
                    course_org.fav_nums -= 1
                    course_org.save()

                elif fav_type == 3:
                    teacher = Teacher.objects.get(id=fav_id)
                    teacher.fav_nums -= 1
                    teacher.save()
                return JsonResponse({"status": "success", "msg": "收藏"})
            else:
                user_fav = UserFavorite()
                user_fav.fav_id = fav_id
                user_fav.fav_type = fav_type
                user_fav.user = request.user
                user_fav.save()
                return JsonResponse({"status": "success", "msg": "已收藏"})

        else:
            return JsonResponse({"status": "fail", "msg": "参数错误"})


class AddCommentView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"status": "fail", "msg": "用户未登录"})
        course_comments_form = CourseCommentForm(request.POST)
        if course_comments_form.is_valid():
            course = course_comments_form.cleaned_data["course"]
            comments = course_comments_form.cleaned_data["comments"]
            course_comments = CourseComments()
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return JsonResponse({"status": "success", "msg": "评论成功"})
        else:
            return JsonResponse({"status": "fail", "msg": "参数错误"})


class HaveLearn(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"status": "fail", "msg": "用户未登录"})
        user_course_form = UserCourseForm(request.POST)
        if user_course_form.is_valid():
            course = user_course_form.cleaned_data["course"]
            # 判断用户是否已经学习
            existed_records = UserCourse.objects.filter(user=request.user, course_id=course.id)
            if existed_records:
                return JsonResponse({"status": "success", "msg": "继续学习"})
            else:
                user_course = UserCourse()
                user_course.course = course
                user_course.user = request.user
                course_see = Course.objects.get(id=course.id)
                course_see.students += 1
                course_see.save()
                user_course.save()
                return JsonResponse({"status": "success", "msg": "开始学习"})
        else:
            return JsonResponse({"status": "fail", "msg": "参数错误"})
