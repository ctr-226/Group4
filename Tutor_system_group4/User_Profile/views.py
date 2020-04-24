from typing import Any, Union

from django.db import models
from django.shortcuts import render

from .models import Student, Teacher
from .forms import UserRegisterForm, UserLoginForm, StudentProfileForm, TeacherProfileForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth

# , UserLoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# 学生信息编辑
@login_required(login_url='/user/login/')
def student_profile_update(request,id):
	#user = User.objects.get(id=id)
	student_profile = Student.objects.get(student_user_id=id)
	if request.method == 'POST':
		if request.user != user:
			return HttpResponse("你没有权限修改此用户信息。")
		student_form = StudentProfileForm(request.POST)
		if student_form.is_valid():
			profile_cd = student_form.cleaned_data
			student_profile.age = profile_cd['age']
			student_profile.gender = profile_cd['gender']
			student_profile.grade = profile_cd['grade']
			student_profile.save()
			return redirect("User_Profile:student_profile_update", id=id)
		else:
			return HttpResponse("注册表单输入有误。请重新输入~")
	elif request.method == 'GET':
		student_form = StudentProfileForm()
		context = {'form': student_form}
		return render(request, 'User_Profile/student_profile_update.html', context)
	else:
		return HttpResponse("请使用GET或POST请求数据")

# 老师信息编辑
@login_required(login_url='/user/login/')
def teacher_profile_update(request,id):
	if request.method == 'POST':
		teacher_form = TeacherProfileForm(request.POST)
	elif request.method == 'GET':
		teacher_form = TeacherProfileForm()
		context = {'form': teacher_form}
		return render(request, 'User_Profile/teacher_profile_update.html', context)
	else:
		return HttpResponse("请使用GET或POST请求数据")


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
			if user_attribute == '0':

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
