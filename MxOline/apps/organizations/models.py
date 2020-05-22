from django.db import models
from django.db.models import Max

from apps.users.models import UserProfile
from apps.users.models import BaseModel


# Create your models here.
class City(BaseModel):
    city_name = models.CharField(max_length=10, verbose_name="城市名", default="北京")
    desc = models.CharField(max_length=100, verbose_name="城市描述", default="")

    class Meta:
        verbose_name = "城市信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.city_name


class CourseOrg(BaseModel):
    org_name = models.CharField(max_length=30, verbose_name="机构名称")
    org_tag = models.CharField(max_length=20, verbose_name="机构标签", default="")
    org_category = models.CharField(max_length=20, verbose_name="机构类别",
                                    choices=(("training", "培训机构"), ("personal", "个人"), ("college", "高校")))
    click_nums = models.IntegerField(verbose_name="点击量", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏人数", default=0)
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="logo", max_length=100)
    org_address = models.CharField(verbose_name="机构地址", max_length=200)
    students = models.IntegerField(verbose_name="学习人数", default=0)
    courses_num = models.IntegerField(verbose_name="课程数", default=0)
    is_legalize = models.BooleanField(verbose_name="是否认证", default=False)
    is_gold_Award = models.BooleanField(verbose_name="是否金牌", default=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在城市")

    def courses(self):
        courses = self.course_set.filter(is_classics=True)[:3]
        return courses

    def teachercount(self):
        teacher_num = self.teacher_set.all().count()
        return teacher_num

    class Meta:
        verbose_name = "机构信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.org_name


class Teacher(BaseModel):
    user = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="用户")
    teacher_name = models.CharField(max_length=10, verbose_name="教师名")
    work_experience = models.IntegerField(verbose_name="工作年限", default=0)
    work_company = models.CharField(verbose_name="就职公司", max_length=20, default="")
    position = models.CharField(verbose_name="公司职位", max_length=10)
    teaching_characteristics = models.TextField(max_length=300, verbose_name="教学特点", default="")
    fav_nums = models.IntegerField(verbose_name="收藏人数", default=0)
    click_nums = models.IntegerField(verbose_name="点击量", default=0)
    age = models.IntegerField(verbose_name="年龄", default=0)
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="头像", max_length=100)
    affiliation = models.ForeignKey(CourseOrg, verbose_name="所属机构", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "教师信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.teacher_name

    def course_nums(self):
        return self.course_set.all().count()

    def hot(self):
        max_nums = self.course_set.aggregate(Max("click_nums"))['click_nums__max']
        return self.course_set.all().filter(click_nums=max_nums)
