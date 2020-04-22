# 导入数据模型ArticlePost
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .forms import UserRegisterForm, UserLoginForm
from .models import Teacher, Student


# 登入
def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            # 清洗出合法数据
            username = user_login_form.cleaned_data['username']
            password = user_login_form.cleaned_data['password']
            user_attribute = user_login_form.cleaned_data['user_attribute']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                # if user.is_student
                # 将用户数据保存在 session 中，即实现了登录动作

                return HttpResponse("登陆成功")
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
