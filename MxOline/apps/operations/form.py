from apps.operations.models import *
from django import forms


class UserFavForm(forms.ModelForm):
    class Meta:
        model = UserFavorite
        fields = ["fav_id", "fav_type"]


class UserCourseForm(forms.ModelForm):
    class Meta:
        model = UserCourse
        fields = ["course"]


class CourseCommentForm(forms.ModelForm):
    class Meta:
        model = CourseComments
        fields = ["course", "comments"]
