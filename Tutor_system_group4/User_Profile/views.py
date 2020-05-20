# 导入数据模型
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse
from django.db import models

from .models import Teacher, Student, User
from .forms import UserRegisterForm, UserLoginForm, StudentProfileForm, TeacherProfileForm

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

User = get_user_model()


# 信息编辑
@login_required(login_url='/user/login/')
def student_profile_update(request, id):
    user = User.objects.get(id=id)
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
            return HttpResponse("注册表单输入有误。请重新输入")

    elif request.method == 'GET':
        student_form = StudentProfileForm()
        context = {'form': student_form}
        return render(request, 'User_Profile/student_profile_update.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


@login_required(login_url='/user/login/')
def teacher_profile_update(request, id):
    user = User.objects.get(id=id)
    teacher_profile = Teacher.objects.get(teacher_user_id=id)

    if request.method == 'POST':
        if request.user != user:
            return HttpResponse("你没有权限修改此用户信息。")

        teacher_form = TeacherProfileForm(request.POST)
        if teacher_form.is_valid():
            profile_cd = teacher_form.cleaned_data
            teacher_profile.age = profile_cd['age']
            teacher_profile.gender = profile_cd['gender']
            teacher_profile.grade = profile_cd['grade']
            teacher_profile.save()
            return redirect("User_Profile:teacher_profile_update", id=id)
        else:
            return HttpResponse("注册表单输入有误。请重新输入")

    elif request.method == 'GET':
        teacher_form = TeacherProfileForm()
        context = {'form': teacher_form}
        return render(request, 'User_Profile/teacher_profile_update.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


# 登入
def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            # 清洗出合法数据
            username = user_login_form.cleaned_data['username']
            password = user_login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                # 此处在redirect时应想办法传入id参数
                id = user.id
                if user.is_student == True:
                    return redirect("User_Profile:student_profile_update", id=id)
                elif user.is_teacher == True:
                    return redirect("User_Profile:teacher_profile_update", id=id)
            else:
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        return render(request, 'User_Profile/login.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


# 登出
def user_logout(request):
    logout(request)
    return redirect("User_Profile:login")


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
                new_user.is_teacher = True
                new_user.save()
                # 如果直接使用objects.create()方法后不需要使用save()
                teacher_profile = Teacher(teacher_user=new_user)
                teacher_profile.name = username
                teacher_profile.mailbox = email
                teacher_profile.phone = phone
                teacher_profile.save()
            else:
                new_user.is_student = True
                new_user.save()
                student_profile = Student(student_user=new_user)
                student_profile.name = username
                student_profile.mailbox = email
                student_profile.phone = phone
                student_profile.save()
            return HttpResponseRedirect('/user/login/')

        #else:
            #return HttpResponse("注册表单输入有误。请重新输入~")

    else:
        form = UserRegisterForm()
        return render(request, 'User_Profile/register.html', {'form': form})
