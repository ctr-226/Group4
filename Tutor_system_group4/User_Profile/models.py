from django.db import models
# 导入内建的User模型。
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import get_user_model

# timezone 用于处理时间相关事务。
from django.utils import timezone
from django.conf import settings


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


User = get_user_model()


# REQUIRED_FIELDS = ['is_student', 'is_teacher']


# 学生数据模型
class Student(models.Model):
    student_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                        related_name='student_profile')
    # 学生姓名 最长100字符
    name = models.CharField(max_length=100, default=' ',verbose_name='姓名')

    # 学生年龄 限定正整数
    age = models.PositiveIntegerField(verbose_name='年龄',blank=True,null=True)

    # 学生性别 choice (u'内部存储名，u'外部显示名')
    GENDER_CHOICE = ((u'M', u'男'), (u'F', u'女'))

    gender = models.CharField(max_length=2, choices=GENDER_CHOICE, default=u'M')

    # 学生年级 choice (u'内部存储名，u'外部显示名')
    GRADE_CHOICE_STUDENT = (
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

    grade = models.CharField(max_length=2, choices=GRADE_CHOICE_STUDENT, default=u'5',verbose_name='年级')

    # 邮箱
    mailbox = models.EmailField(verbose_name='个人邮箱')

    # 联系电话
    phone = models.CharField(max_length=12,verbose_name='联系电话')

    # 个人简介
    briefintroduction = models.CharField(verbose_name="教师信息", blank=True, null=True, max_length=100,
                                         default="暂无", help_text="个人简介，所在学校/学习情况等")

    # 头像
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d/',default='default.jpg', verbose_name='头像',blank=True,null=True)

    class Meta:
        verbose_name = "学生"
    
    def __str__(self):
        #  self.name 将学生姓名返回
        return self.name


# 教师数据模型暂时去掉了独一无二性
class Teacher(models.Model):
    teacher_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                        related_name='teacher_profile')
    # 教师姓名 最长100字符
    name = models.CharField(max_length=100, blank=True,verbose_name="姓名")
    # 教师年龄 限定正整数
    age = models.PositiveIntegerField(blank=True,default=20,verbose_name="年龄")

    # 教师性别 choice (u'内部存储名，u'外部显示名')
    GENDER_CHOICE = (
        (u'M', u'男'),
        (u'F', u'女')
    )

    gender = models.CharField(max_length=2, choices=GENDER_CHOICE, default=u'M')

    # 教师年级
    GRADE_CHOICE_TEACHER = (
        (u'0', u'大一'),
        (u'1', u'大二'),
        (u'2', u'大三'),
        (u'3', u'大四'),
        (u'4', u'研一'),
        (u'5', u'研二'),
        (u'6', u'研三'),
        (u'7', u'其他')
    )

    grade = models.CharField(verbose_name="教师年级",max_length=2, choices=GRADE_CHOICE_TEACHER, default=u'1')

    # 邮箱
    mailbox = models.EmailField(verbose_name="电子邮箱")

    # 联系电话
    phone = models.CharField(verbose_name="联系电话",max_length=12)

    # 个人简介
    briefintroduction = models.CharField(verbose_name="教师信息", blank=True, null=True, max_length=100,
                                          default="暂无", help_text="个人简介，所在学院/专业/履历等")

    # 头像
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d/',default='default.jpg', verbose_name='头像',blank=True,null=True)

    class Meta:
        verbose_name = "家教"

    def __str__(self):
        # return self.name 将老师姓名返回
        return self.name
