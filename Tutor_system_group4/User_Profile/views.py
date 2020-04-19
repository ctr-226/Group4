from typing import Any, Union

from django.db import models
from django.shortcuts import render

# 导入数据模型ArticlePost
from .models import Teacher, Student
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserRegisterForm
# , UserLoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# 登入
def user_login(request):
	context = {}
	return render(request, 'User_Profile/login.html', context)


# 登出
def user_logout(request):
	context = {}
	return render(request, 'User_Profile/logout.html', context)


# 注册
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password2']
			phone = form.cleaned_data['phone']
			user_attribute = form.cleaned_data['user_attribute']
			# 使用内置User自带create_user方法创建用户，不需要使用save()
			new_user = User.objects.create_user(username=username, password=password)
			if user_attribute == 0:

				# 如果直接使用objects.create()方法后不需要使用save()
				teacher_profile = Teacher(teacher_user=new_user)
				teacher_profile.name = username
				teacher_profile.mailbox = email
				teacher_profile.phone = phone
				teacher_profile.save()
			else:
				student_profile = Student(student_user=new_user)
				student_profile.name = username
				student_profile.mailbox = email
				student_profile.phone = phone
				student_profile.save()

			return HttpResponseRedirect('/user/login/')

	else:
		form = UserRegisterForm()
	return render(request, 'User_Profile/register.html', {'form': form})


# 学生信息编辑
def student_profile_update(request):
	context = {}
	return render(request, 'User_Profile/student_profile_update.html', context)


# 老师信息编辑
def teacher_profile_update(request):
	context = {}
	return render(request, 'User_Profile/teacher_profile_update.html', context)
