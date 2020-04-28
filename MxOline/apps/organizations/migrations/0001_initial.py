# Generated by Django 2.2 on 2020-04-28 23:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('city_name', models.CharField(default='北京', max_length=10, verbose_name='城市名')),
                ('desc', models.CharField(default='', max_length=100, verbose_name='城市描述')),
            ],
            options={
                'verbose_name': '城市信息',
                'verbose_name_plural': '城市信息',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('org_name', models.CharField(max_length=30, verbose_name='机构名称')),
                ('org_tag', models.CharField(default='', max_length=20, verbose_name='机构标签')),
                ('org_category', models.CharField(choices=[('training', '培训机构'), ('personal', '个人'), ('college', '高校')], max_length=20, verbose_name='机构类别')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击量')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('image', models.ImageField(upload_to='org/%Y/%m', verbose_name='logo')),
                ('org_address', models.CharField(max_length=200, verbose_name='机构地址')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('courses_num', models.IntegerField(default=0, verbose_name='课程数')),
                ('is_legalize', models.BooleanField(default=False, verbose_name='是否认证')),
                ('is_gold_Award', models.BooleanField(default=False, verbose_name='是否金牌')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.City', verbose_name='所在城市')),
            ],
            options={
                'verbose_name': '机构信息',
                'verbose_name_plural': '机构信息',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('teacher_name', models.CharField(max_length=10, verbose_name='教师名')),
                ('work_experience', models.IntegerField(default=0, verbose_name='工作年限')),
                ('work_company', models.CharField(default='', max_length=20, verbose_name='就职公司')),
                ('position', models.CharField(max_length=10, verbose_name='公司职位')),
                ('teaching_characteristics', models.TextField(default='', max_length=300, verbose_name='教学特点')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击量')),
                ('age', models.IntegerField(default=0, verbose_name='年龄')),
                ('image', models.ImageField(upload_to='teacher/%Y/%m', verbose_name='头像')),
                ('affiliation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.CourseOrg', verbose_name='所属机构')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '教师信息',
                'verbose_name_plural': '教师信息',
            },
        ),
    ]