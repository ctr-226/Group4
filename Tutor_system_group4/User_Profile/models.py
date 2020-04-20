from django.db import models
# 导入内建的User模型。
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone


# 学生数据模型
class Student(models.Model):
	student_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
	# 学生姓名 最长100字符
	name = models.CharField(max_length=100, default=' ')

	# 学生年龄 限定正整数
	age = models.PositiveIntegerField(default=15)

	# 学生性别 chioce (u'内部存储名，u'外部显示名')
	GENDER_CHOICE = ((u'M', u'男'), (u'F', u'女'))

	gender = models.CharField(max_length=2, choices=GENDER_CHOICE, default=u'M')

	# 学生年级 chioce (u'内部存储名，u'外部显示名')
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

	grade = models.CharField(max_length=2, choices=GRADE_CHOICE_STUDENT, default=u'5')

	# 邮箱
	mailbox = models.EmailField(unique=True)

	# 联系电话
	phone = models.CharField(max_length=12)

	def __str__(self):
		#  self.id 将文章标题返回
		return self.name


# 教师数据模型暂时去掉了独一无二性
class Teacher(models.Model):
	teacher_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
	# 教师姓名 最长100字符
	name = models.CharField(max_length=100, blank=True)
	# 教师年龄 限定正整数
	age = models.PositiveIntegerField(default=20)

	# 教师性别 chioce (u'内部存储名，u'外部显示名')
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

	grade = models.CharField(max_length=2, choices=GRADE_CHOICE_TEACHER, default=u'1')

	# 邮箱
	mailbox = models.EmailField(unique=True)

	# 联系电话
	phone = models.CharField(max_length=12)

	# 一对多关系
	student_teached = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		# return self.id 将文章标题返回
		return self.name
