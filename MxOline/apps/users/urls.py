from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.users.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user-info/', UserCenterView.as_view(), name='user_info'),
    path('user-course/',
         login_required(TemplateView.as_view(template_name='operations/usercenter-mycourse.html'), login_url="/login/",
                        ), {"current_page": 'course'}, name='user_course'),
    path('user-fav/', UserfavView.as_view(), name='user_fav'),
    path('user-msg/', UserMsgView.as_view(), name='user_msg'),

]
