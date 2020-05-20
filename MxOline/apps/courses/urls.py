from django.urls import path, re_path
from apps.courses.views import *

urlpatterns = [
    re_path('^list/', CoursesView.as_view(), name='course_list'),
    re_path(r'^(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='detail'),
    re_path(r'^(?P<course_id>\d+)/lesson/$', CourseLessonView.as_view(), name='lesson'),
    re_path(r'^(?P<course_id>\d+)/comment/$', CourseCommentView.as_view(), name='comment'),
    re_path(r'^(?P<course_id>\d+)/video/(?P<video_id>\d+)/$', CourseVideoView.as_view(), name='video'),
]
