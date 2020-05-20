from django.conf.urls import url

from apps.operations.views import AddFavView, AddCommentView, HaveLearn

urlpatterns = [
    url(r'^fav/$', AddFavView.as_view(), name='fav'),
    url(r'^have/$', HaveLearn.as_view(), name='have'),
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),

]
