from django.shortcuts import render
from django.views.generic import View
from apps.courses.models import *
from django.shortcuts import render_to_response
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


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
