# Generated by Django 3.0.3 on 2020-05-27 07:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=50, verbose_name='课程名称')),
                ('grade_course', models.CharField(choices=[('0', '小学一年级至三年级'), ('1', '小学四年级至六年级'), ('2', '初一'), ('3', '初二'), ('4', '初三'), ('5', '高一'), ('6', '高二'), ('7', '高三'), ('8', '其他')], max_length=2, verbose_name='学生年级')),
                ('subject', models.CharField(choices=[('zh', '语文'), ('math', '数学'), ('en', '英语'), ('phy', '物理'), ('che', '化学'), ('bio', '生物'), ('pol', '政治'), ('his', '历史'), ('geo', '地理')], max_length=10, verbose_name='科目')),
                ('introduction', models.CharField(default='', max_length=150, verbose_name='简介')),
                ('charge', models.IntegerField(default=0, verbose_name='课程收费')),
                ('comment', models.CharField(blank=True, default='暂无', max_length=100, null=True, verbose_name='评论')),
                ('time_set', models.TimeField(auto_now_add=True)),
                ('time_match', models.TimeField(default=django.utils.timezone.now)),
                ('state_match', models.BooleanField()),
            ],
        ),
    ]
