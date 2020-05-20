from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View
from apps.courses.models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from apps.operations.models import UserFavorite, UserCourse, CourseComments


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
        has_learn = False
        print(UserCourse.objects.filter(user=request.user, course_id=course.id))
        if request.user.is_authenticated:
            # 查询用户是否收藏了该课程和机构 fav_type=1证明是课程收藏，如果有，证明用户收藏了这个课
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=2):
                has_fav_org = True
            if UserCourse.objects.filter(user=request.user, course_id=course.id):
                has_learn = True

        tags = course.coursetag_set.all()
        tag_list = [tag.tag for tag in tags]
        relative_courses = []
        if tags:
            course_tags = CourseTag.objects.filter(tag__in=tag_list).exclude(course=course)[:3]
            for course_tag in course_tags:
                relative_courses.append(course_tag.course)
                print(relative_courses)

        return render(request, 'courses/course-detail.html',
                      {"course": course, "has_fav_course": has_fav_course, "has_fav_org": has_fav_org,
                       "relative_courses": relative_courses, "has_learn": has_learn})


class CourseLessonView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        course_resource = CourseResource.objects.filter(course=course)

        # 学习记录 I、查询当前用户的学习记录
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user_id for user_course in user_courses]
        have_learn = UserCourse.objects.filter(user_id__in=user_ids).order_by("-course__click_nums")[0:5]

        have_learn_expect = []
        for item in have_learn:
            if item.course.id != course_id:
                have_learn_expect.append(item.course)

        return render(request, 'courses/course-video.html',
                      {"course": course, "course_resource": course_resource, "have_learn_expect": have_learn_expect})


class CourseCommentView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        course_resource = CourseResource.objects.filter(course=course)
        comments = CourseComments.objects.filter(course=course)

        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user_id for user_course in user_courses]
        have_learn = UserCourse.objects.filter(user_id__in=user_ids).order_by("-course__click_nums")[0:5]

        have_learn_expect = []
        for item in have_learn:
            if item.course.id != course_id:
                have_learn_expect.append(item.course)

        return render(request, 'courses/course-comment.html',
                      {"course": course, "comments": comments, "course_resource": course_resource,
                       "have_learn_expect": have_learn_expect})


class CourseVideoView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, course_id, video_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        video = Video.objects.get(id=int(video_id))
        course_resource = CourseResource.objects.filter(course=course)

        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user_id for user_course in user_courses]
        have_learn = UserCourse.objects.filter(user_id__in=user_ids).order_by("-course__click_nums")[0:5]

        have_learn_expect = []
        for item in have_learn:
            if item.course.id != course_id:
                have_learn_expect.append(item.course)
        return render(request, 'courses/course-play.html',
                      {"course": course, "video": video, "course_resource": course_resource,
                       "have_learn_expect": have_learn_expect})
