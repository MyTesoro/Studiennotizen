from django.urls import path
from apps.users.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='users/index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
