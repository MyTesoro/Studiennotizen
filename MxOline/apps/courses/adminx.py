import xadmin
from apps.courses.models import Course, Lesson, Video, CourseResource, CourseTag


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'teacher__teacher_name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    list_editable = ["degree", "desc"]


class LessonAdmin(object):
    list_display = ['course', 'chapter_name', 'add_time']
    search_fields = ['course', 'chapter_name']
    list_filter = ['course__name', 'chapter_name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'video_name', 'add_time']
    search_fields = ['lesson', 'video_name']
    list_filter = ['lesson', 'video_name', 'add_time']


class CourseTagAdmin(object):
    list_display = ['course', 'tag', 'add_time']
    search_fields = ['course', 'tag']
    list_filter = ['course', 'tag', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'resource_name', 'file_url', 'add_time']
    search_fields = ['course', 'resource_name', 'file_url']
    list_filter = ['course', 'resource_name', 'file_url', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseTag, CourseTagAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)


