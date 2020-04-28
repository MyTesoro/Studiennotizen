from django.db import models
from apps.users.models import BaseModel


# Create your models here.

class Course(BaseModel):
    name = models.CharField(verbose_name="课程名", max_length=50)
    desc = models.CharField(verbose_name="课程描述", max_length=300)
    learn_times = models.IntegerField(default=0, verbose_name="学习时长/min")
    degree = models.CharField(verbose_name="课程难度",
                              choices=(('primary', '初级'), ('intermediate', '中级'), ('advanced', '高级')), max_length=20)
    students = models.IntegerField(verbose_name="学习人数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏人数", default=0)
    click_nums = models.IntegerField(verbose_name="点击量", default=0)
    notice = models.CharField(verbose_name="课程公告", max_length=300, default="")
    category = models.CharField(verbose_name="课程类别", max_length=20, default="后端开发")
    tag = models.CharField(verbose_name="标签", max_length=10, default="")
    course_notes = models.CharField(verbose_name="课程须知", max_length=300, default="")
    teacher_notice = models.CharField(verbose_name="教师通告", max_length=300, default="")
    is_classic = models.BooleanField(default=False, verbose_name="是否经典")
    is_banner = models.BooleanField(default=False, verbose_name="是否广告位")
    course_image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="封面", max_length=100)

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    # on_delete 表示对应的外键数据被删除后当前数据如何执行
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    chapter_name = models.CharField(verbose_name="章节名", max_length=100)
    learn_times = models.IntegerField(default=0, verbose_name="学习时长/min")

    class Meta:
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.chapter_name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name="章节", on_delete=models.CASCADE)
    video_name = models.CharField(max_length=100, verbose_name="视频名称")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长/min")
    url = models.CharField(max_length=1000, verbose_name="访问地址")

    class Meta:
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.video_name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    resource_name = models.CharField(max_length=100, verbose_name="名称")
    file_url = models.FileField(max_length=200, verbose_name="下载地址", upload_to="courses/resourse%Y/%m")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.resource_name
