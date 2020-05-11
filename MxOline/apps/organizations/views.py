from django.shortcuts import render
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
        org_nums = all_orgs.count()

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

        org_nums = all_orgs.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # per_page每页显示多少个
        p = Paginator(all_orgs, per_page=5, request=request)
        orgs = p.page(page)
        return render(request, 'organizations/org-list.html',
                      {"orgs": orgs, "org_nums": org_nums, "all_city": all_city, 'category': category,
                       "city_id": city_id, "advence_list": advence_list})


class OrgAskView(View):
    # 用户咨询木块
    def post(self, request, *args, **kwargs):
        ask_form = OrgAskForm(request.POST)
        if ask_form.is_valid():
            ask_form.save(commit=True)
            return JsonResponse({"status": "success", "msg": "commit_success"})
        else:
            return JsonResponse({"status": "fail", "msg": "commit_error"})
