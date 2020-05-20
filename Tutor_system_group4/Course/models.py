from django.db import models

# Create your models here.

from User_Profile.models import Student, Teacher
from django.utils import timezone


class CourseDetail(models.Model):
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.SET_NULL)

    nick_name = models.CharField(verbose_name='课程名称' ,max_length=50, blank=True)

    GRADE_CHOICE_COURSE = (
        (u'0', u'小学一年级至三年级'),
        (u'1', u'小学四年级至六年级'),
        (u'2', u'初一'),
        (u'3', u'初二'),
        (u'4', u'初三'),
        (u'5', u'高一'),
        (u'6', u'高二'),
        (u'7', u'高三'),
        (u'8', u'其他')
    )
    grade_course = models.CharField(max_length=2, choices=GRADE_CHOICE_COURSE,verbose_name='学生年级')

    SUBJECT_CHOICE = (
        ('zh', '语文'),
        ('math', '数学'),
        ('en', '英语'),
        ('phy', '物理'),
        ('che', '化学'),
        ('bio', '生物'),
        ('pol', '政治'),
        ('his', '历史'),
        ('geo', '地理'),
    )
    subject = models.CharField(max_length=10, choices=SUBJECT_CHOICE, verbose_name='科目')

    # 简介
    introduction = models.CharField(max_length=150, default='', verbose_name='简介')

    # 课程收费估计
    charge = models.IntegerField(verbose_name='课程收费', default=0)

    # 评论
    comment = models.CharField(max_length=100, blank=True, null=True, verbose_name='评论')

    # 课程设立的时间
    time_set = models.TimeField(auto_now_add=True)

    # 课程成功匹配的时间
    time_match = models.TimeField(default=timezone.now)

    # 课程是否匹配，1=匹配成功 0=未匹配成功
    state_match = models.BooleanField()

    # 课程和学生多对一关系，记录成功匹配的学生
    student_agreed = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL,
                                       verbose_name='成功匹配', related_name='agreed_Student')

    # 课程和学生多对多关系，记录申请选课的学生
    student_applied = models.ManyToManyField(Student, related_name='applied_Student', verbose_name='申请学员',blank=True)

    class Mata:
        verbose_name='课程'

    # 返回课程名
    def __str__(self):
        return self.nick_name
