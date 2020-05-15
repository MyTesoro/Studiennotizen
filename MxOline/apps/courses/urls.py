from django.urls import path,re_path
from apps.courses.views import *



urlpatterns = [
    re_path('^list/', CoursesView.as_view(), name='course_list'),
    re_path(r'^(?P<course_id>\d+)', CourseDetailView.as_view(), name='detail'),
]
