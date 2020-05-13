from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import CourseDetail
from .forms import CourseForm
# Create your views here.

@login_required(login_url='/user/login/')
def increase_course(request,teacher_id):
    user = User.objects.get(id=teacher_id)
    if user.is_teacher == True:
        if request.method == "POST":
            if request.user != user:
                return HttpResponse("你没有权限修改此用户信息。")

            course_form = CourseForm(request.POST)
            if course_form.is_valid():
                new_course = course_form.save(commit=False)
                #可能还要存一些表单给不了的数据
                new_course.save()
                return redirect("Course:increase_course",teacher_id=teacher_id)

        elif request.method == "GET":
            course_form = CourseForm()
            context = {'form': course_form}
            return render(request, 'Course/increase_course.html', context)
        else:
            return HttpResponse("请使用GET或POST请求数据")
    else:
        return HttpResponse("只有老师才能开设新课程哦")


