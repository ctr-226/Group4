# 引入表单类
from django import forms
# 引入 User 模型 ，用户数据都存在这一模型对应数据库中
from django.contrib.auth.models import User
# 引入 Profile 模型
from .models import Student,Teacher

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher