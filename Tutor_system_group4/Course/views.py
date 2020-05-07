from django.shortcuts import render
from User_Profile.models import Student
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .models import CourseDetail
from django.contrib.auth.decorators import login_required


# Create your views here.
#课程申请匹配
def match(request):
    return None

#增加课程
def increase_course(request):
    return None

#同意申请
def agree_match(request):
    return None

#课程详细内容

def detail_course(request, id):
    course = CourseDetail.objects.get(id=id)
    context = { 'course':course }
    return render(request,'Course/detail.html',context )


#课程管理
def manage_course(request, id):
    return None
