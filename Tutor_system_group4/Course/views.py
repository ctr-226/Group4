from User_Profile.models import Student, User
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth

from .forms import CourseForm
from .models import CourseDetail


# Create your views here.
# 首页导航
def index(request):
    if request.user.is_authenticated:
        # 初步筛选未匹配课程
        Course = CourseDetail.objects.filter(state_match=0)
        if request.method == 'GET':
            # 获取前端筛选选项
            gender_choice = request.GET.get("gender", '')
            subject_choice = request.GET.get("subject", '')
            grade_choice = request.GET.get("grade", '')
            charge_choice = request.GET.get("charge", '')
            # 条件判断筛选课程
            if gender_choice == "0" or gender_choice == '':
                if subject_choice == "0" or subject_choice == '':
                    if grade_choice == "9" or grade_choice == '':
                        if charge_choice == "1":
                            Course_show = Course.filter(charge__lte=30)
                        elif charge_choice == "2":
                            Course_show = Course.filter(charge__range=[30, 50])
                        elif charge_choice == "3":
                            Course_show = Course.filter(charge__range=[50, 70])
                        elif charge_choice == "4":
                            Course_show = Course.filter(charge__range=[70, 100])
                        elif charge_choice == "5":
                            Course_show = Course.filter(charge__gt=100)
                        else:
                            Course_show = Course
                    else:
                        if charge_choice == "1":
                            Course_show = Course.filter(charge__lte=30).filter(grade_course=grade_choice)
                        elif charge_choice == "2":
                            Course_show = Course.filter(charge__range=[30, 50]).filter(grade_course=grade_choice)
                        elif charge_choice == "3":
                            Course_show = Course.filter(charge__range=[50, 70]).filter(grade_course=grade_choice)
                        elif charge_choice == "4":
                            Course_show = Course.filter(charge__range=[70, 100]).filter(grade_course=grade_choice)
                        elif charge_choice == "5":
                            Course_show = Course.filter(charge__gt=100).filter(grade_course=grade_choice)
                        else:
                            Course_show = Course.filter(grade_course=grade_choice)
                else:
                    if grade_choice == "0" or grade_choice == '':
                        if charge_choice == "1":
                            Course_show = Course.filter(charge__lte=30).filter(subject=subject_choice)
                        elif charge_choice == "2":
                            Course_show = Course.filter(charge__range=[30, 50]).filter(subject=subject_choice)
                        elif charge_choice == "3":
                            Course_show = Course.filter(charge__range=[50, 70]).filter(subject=subject_choice)
                        elif charge_choice == "4":
                            Course_show = Course.filter(charge__range=[70, 100]).filter(subject=subject_choice)
                        elif charge_choice == "5":
                            Course_show = Course.filter(charge__gt=100).filter(subject=subject_choice)
                        else:
                            Course_show = Course.filter(subject=subject_choice)
                    else:
                        if charge_choice == "1":
                            Course_show = Course.filter(charge__lte=30).filter(grade_course=grade_choice).filter(subject=subject_choice)
                        elif charge_choice == "2":
                            Course_show = Course.filter(charge__range=[30, 50]).filter(grade_course=grade_choice).filter(subject=subject_choice)
                        elif charge_choice == "3":
                            Course_show = Course.filter(charge__range=[50, 70]).filter(grade_course=grade_choice).filter(subject=subject_choice)
                        elif charge_choice == "4":
                            Course_show = Course.filter(charge__range=[70, 100]).filter(grade_course=grade_choice).filter(subject=subject_choice)
                        elif charge_choice == "5":
                            Course_show = Course.filter(charge__gt=100).filter(grade_course=grade_choice).filter(subject=subject_choice)
                        else:
                            Course_show = Course.filter(grade_course=grade_choice).filter(subject=subject_choice)
            else:
                if subject_choice == "0" or subject_choice == '':
                    if grade_choice == "0" or grade_choice == '':
                        if charge_choice == "1":
                            Course_show = Course.filter(charge__lte=30)
                        elif charge_choice == "2":
                            Course_show = Course.filter(charge__range=[30, 50])
                        elif charge_choice == "3":
                            Course_show = Course.filter(charge__range=[50, 70])
                        elif charge_choice == "4":
                            Course_show = Course.filter(charge__range=[70, 100])
                        elif charge_choice == "5":
                            Course_show = Course.filter(charge__gt=100)
                        else:
                            Course_show = Course
                    else:
                        if charge_choice == "1":
                            Course_show = Course.filter(charge__lte=30).filter(grade_course=grade_choice)
                        elif charge_choice == "2":
                            Course_show = Course.filter(charge__range=[30, 50]).filter(grade_course=grade_choice)
                        elif charge_choice == "3":
                            Course_show = Course.filter(charge__range=[50, 70]).filter(grade_course=grade_choice)
                        elif charge_choice == "4":
                            Course_show = Course.filter(charge__range=[70, 100]).filter(grade_course=grade_choice)
                        elif charge_choice == "5":
                            Course_show = Course.filter(charge__gt=100).filter(grade_course=grade_choice)
                        else:
                            Course_show = Course.filter(grade_course=grade_choice)
                else:
                    if grade_choice == "0" or grade_choice=='':
                        if charge_choice == "1":
                            Course_show = Course.filter(charge__lte=30).filter(subject=subject_choice)
                        elif charge_choice == "2":
                            Course_show = Course.filter(charge__range=[30, 50]).filter(subject=subject_choice)
                        elif charge_choice == "3":
                            Course_show = Course.filter(charge__range=[50, 70]).filter(subject=subject_choice)
                        elif charge_choice == "4":
                            Course_show = Course.filter(charge__range=[70, 100]).filter(subject=subject_choice)
                        elif charge_choice == "5":
                            Course_show = Course.filter(charge__gt=100).filter(subject=subject_choice)
                        else:
                            Course_show = Course.filter(state_match=0)
                    else:
                        if charge_choice == "1":
                            Course_show = Course.filter(charge__lte=30).filter(grade_course=grade_choice).filter(subject=subject_choice)
                        elif charge_choice == "2":
                            Course_show = Course.filter(charge__range=[30, 50]).filter(grade_course=grade_choice).filter(subject=subject_choice)
                        elif charge_choice == "3":
                            Course_show = Course.filter(charge__range=[50, 70]).filter(grade_course=grade_choice).filter(subject=subject_choice)
                        elif charge_choice == "4":
                            Course_show = Course.filter(charge__range=[70, 100]).filter(grade_course=grade_choice).filter(subject=subject_choice)
                        elif charge_choice == "5":
                            Course_show = Course.filter(charge__gt=100).filter(grade_course=grade_choice).filter(subject=subject_choice)
                        else:
                            Course_show = Course.filter(grade_course=grade_choice).filter(subject=subject_choice)

            # 展示课程向前端
            context = {'course': Course_show}
            return render(request, 'filter.html', context)
        else:
            return HttpResponse("请使用GET请求数据")
    else:
        return render(request, 'index.html')


@login_required(login_url='/user/login/')
def filter(request):
    return render(request, 'filter.html')


# 增加课程
@login_required(login_url='/user/login/')
def increase_course(request):
    user = User.objects.get(id=request.user.id)
    if user.is_teacher == True:
        if request.method == "POST":
            if request.user != user:
                return HttpResponse("你没有权限修改此用户信息。")

            course_form = CourseForm(request.POST)
            if course_form.is_valid():
                new_course = course_form.save(commit=False)
                # 还要存一些表单给不了的数据
                new_course.teacher = user
                new_course.state_match = False
                new_course.save()
                return redirect("Course:increase_course")

        elif request.method == "GET":
            course_form = CourseForm()
            context = {'form': course_form}
            return render(request, 'Course/increase_course.html', context)
        else:
            return HttpResponse("请使用GET或POST请求数据")
    else:
        return HttpResponse("只有老师才能开设新课程哦")


# 课程申请匹配
def match(request, coursedetail_id):
    course_applying = CourseDetail.objects.get(id=coursedetail_id)
    applicant = User.objects.get(id=request.user.id)
    # 虽然这里有判断，但还是尽量在前端控制只有学生浏览课程详情页面时才有“申请”的按钮
    if applicant.is_student == True:
        # 多对多中间表加一个元组
        course_applying.student_applied.add(applicant)
        course_applying.save()
        return redirect('Course: detail_course')
    else:
        return HttpResponse("只有学生可以申请选课")
    return redirect('Course: detail_course')


# 同意申请
def agree_match(request, coursedetail_id):
    course_applying = CourseDetail.objects.get(id=coursedetail_id)
    selected_student = Student.objects.get(id=request.POST['choice'])
    course_applying.student_agreed = selected_student
    course_applying.state_match = True
    course_applying.save()
    return redirect('Course: manage_course')


# 课程详细内容
def detail_course(request, coursedetail_id):
    course = CourseDetail.objects.get(id=coursedetail_id)
    context = {'course': course, 'coursedetail_id': coursedetail_id}
    return render(request, 'Course/detail.html', context)


# 课程管理
def manage_course(request):
    ID = request.user.id
    user = User.objects.get(id=ID)
    # context = {}
    if user.is_teacher:

        course_match = user.teacher_profile.coursedetail_set.filter(state_match=True)
        # course_match = CourseDetail.objects.filter(teacher_id=id, state_match=True)
        # course_unmatched = CourseDetail.objects.filter(teacher__id=id, state_match=False)
        course_unmatched = user.teacher_profile.coursedetail_set.filter(state_match=False)
        course_list = {}
        for course in course_unmatched:
            if course.student_applied.all():
                course_list[course] = course.student_applied.all()
        context = {'course_match': course_match, 'course_unmatched': course_unmatched,
                   'course_list': course_list}
        return render(request, 'Course/teacher_subject_detail.html', context)
    if user.is_student:
        course_match = user.student_profile.agreed_Student.filter(state_match=True)
        course_applying = user.student_profile.applied_Student.all()
        context = {'course_match': course_match, 'course_applying': course_applying}

        return render(request, 'Course/student_subject_detail.html', context)

def index2(request):
    return render(request,'index2.html')
