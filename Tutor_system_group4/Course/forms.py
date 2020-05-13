# 引入表单类
from django import forms
# 引入 User 模型 ，用户数据都存在这一模型对应数据库中
from django.contrib.auth.models import User
# 引入 课程 模型
from .models import CourseDetail
import re

class CourseForm(forms.ModelForm):
    class meta:
        model = CourseDetail
        fields = ['nick_name','grade_course', 'subject']