from django.db import models

# Create your models here.

from User_Profile.models import Student, Teacher
from django.utils import timezone


class CourseDetail(models.Model):
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.SET_NULL)

    nick_name = models.CharField(max_length=50, blank=True)

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
    grade_course = models.CharField(max_length=2, choices=GRADE_CHOICE_COURSE)

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
    subject = models.CharField(max_length=10, choices=SUBJECT_CHOICE)
    
    comment = models.CharField(max_length=100, default='')
    
    state_match = models.BooleanField()
