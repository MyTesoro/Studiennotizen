"""MxOline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
import xadmin
from django.conf.urls import url, include
from django.views.static import serve
from MxOline.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),

    # 根路径
    re_path(r'^', include(('apps.users.urls', 'users'), namespace='users')),
    re_path(r'^org/', include(('apps.organizations.urls', 'organizations'), namespace='org')),
    re_path(r'^course/', include(('apps.courses.urls', 'courses'), namespace='course')),
    re_path(r'^opt/', include(('apps.operations.urls', 'operations'), namespace='opt')),

    # 配置上传文件访问的url
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]
