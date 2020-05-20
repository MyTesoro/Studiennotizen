from django.shortcuts import render, redirect
from django.views.generic import View
from apps.organizations.models import *
from django.shortcuts import render_to_response
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.organizations.form import OrgAskForm
from django.http import JsonResponse


# Create your views here.
class OrgView(View):
    def get(self, request, *args, **kwargs):
        # 展示授课机构列表页
        all_orgs = CourseOrg.objects.all()
        all_city = City.objects.all()

        category = request.GET.get("ct", "")
        if category:
            all_orgs = all_orgs.filter(org_category=category)

        # 对所在城市进行筛选
        city_id = request.GET.get('city', "")
        if city_id:
            if city_id.isdigit():
                all_orgs = all_orgs.filter(city_id=int(city_id))

        sort = request.GET.get("sort", "")
        if sort:
            all_orgs = CourseOrg.objects.order_by('-' + str(sort))

        advence_list = CourseOrg.objects.order_by('-click_nums')[0:5]

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # per_page每页显示多少个
        p = Paginator(all_orgs, per_page=5, request=request)
        orgs = p.page(page)

        org_nums = all_orgs.count()
        return render(request, 'organizations/org-list.html',
                      {"orgs": orgs, "org_nums": org_nums, "all_city": all_city, 'category': category,
                       "city_id": city_id, "advence_list": advence_list, "all_orgs": all_orgs, "sort": sort})


class OrgAskView(View):
    # 用户咨询木块
    def post(self, request, *args, **kwargs):
        ask_form = OrgAskForm(request.POST)
        if ask_form.is_valid():
            ask_form.save(commit=True)
            return JsonResponse({"status": "success", "msg": "commit_success"})
        else:
            return JsonResponse({"status": "fail", "msg": "commit_error"})


class TeacherView(View):
    def get(self, request, *args, **kwargs):
        all_teachers = Teacher.objects.all()

        sort = request.GET.get("sort", "")
        if sort:
            all_teachers = CourseOrg.objects.order_by('-' + str(sort))

        advence_list = Teacher.objects.order_by('-click_nums')[0:5]

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # per_page每页显示多少个
        p = Paginator(all_teachers, per_page=5, request=request)
        teachers = p.page(page)

        teacher_nums = all_teachers.count()
        return render(request, "organizations/teachers-list.html",
                      {"all_teachers": all_teachers, "teachers": teachers, "teacher_nums": teacher_nums,
                       "advence_list": advence_list})


class TeacherDetailView(View):

    def get(self, request, teacher_id, *args, **kwargs):
        teacher = Teacher.objects.get(id=int(teacher_id))
        teacher.click_nums += 1
        teacher.save()

        course_t = teacher.course_set.order_by('-click_nums')[:3]

        return render(request, "organizations/teacher-detail.html", {"teacher": teacher, "course_t": course_t})


class OrgDetailView(View):
    def get(self, request, org_id, *args, **kwargs):
        org = CourseOrg.objects.get(id=int(org_id))
        org.click_nums += 1
        org.save()
        print(org.click_nums)
        return render(request, 'organizations/org-detail-homepage.html', {'org': org})


class OrgDescDetailView(View):
    def get(self, request, org_id, *args, **kwargs):
        return render(request, 'organizations/org-detail-desc.html')


class OrgCourseDetailView(View):
    def get(self, request, org_id, *args, **kwargs):
        return render(request, 'organizations/org-detail-course.html')


class OrgTeacherDetailView(View):
    def get(self, request, org_id, *args, **kwargs):
        return render(request, 'organizations/org-detail-teachers.html')
