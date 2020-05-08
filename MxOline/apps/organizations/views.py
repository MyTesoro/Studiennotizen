from django.shortcuts import render
from django.views.generic import View
from apps.organizations.models import *


# Create your views here.
class OrgView(View):
    def get(self, request, *args, **kwargs):
        # 展示授课机构列表页
        all_orgs = CourseOrg.objects.all()
        org_nums = CourseOrg.objects.all().count()
        all_city = City.objects.all()

        return render(request, 'organizations/org-list.html',
                      {"all_orgs": all_orgs, "org_nums": org_nums, "all_city": all_city})
