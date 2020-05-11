# Generated by Django 2.2 on 2020-05-11 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='belong_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.CourseOrg', verbose_name='所属机构'),
        ),
    ]
