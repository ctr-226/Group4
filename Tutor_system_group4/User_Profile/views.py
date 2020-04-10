from django.shortcuts import render

# 导入数据模型ArticlePost
from .models import Teacher,Student

# 登入
def login(request):
    context = {}
    return render(request, 'User_Profile/login.html', context)

# 登出
def logout(request):
    context = {}
    return render(request, 'User_Profile/logout.html', context)

# 注册
def register(request):
    context = {}
    return render(request, 'User_Profile/register.html', context)

# 学生信息编辑
def student_profile_update(request):
    context = {}
    return render(request, 'User_Profile/student_profile_update.html', context)

# 老师信息编辑
def teacher_profile_update(request):
    context = {}
    return render(request, 'User_Profile/teacher_profile_update.html', context)