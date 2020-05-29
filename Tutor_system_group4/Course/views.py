from User_Profile.models import Student, User, Teacher
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CourseForm
from .models import CourseDetail


# 首页筛选
def index(request):
    if request.user.is_authenticated:
        course = CourseDetail.objects.filter(state_match=0)
        context = {'course': course}
        return render(request, 'index2.html', context)
    else:
        return render(request, 'index.html')


# 课程筛选函数
@login_required(login_url='/user/login/')
def filter(request):
    # 初步筛选未匹配课程
    course_0 = CourseDetail.objects.filter(state_match=0)
    if request.method == 'GET':
        # 获取前端筛选选项
        gender_choice = request.GET.get("gender", '')
        subject_choice = request.GET.get("subject", '')
        grade_choice = request.GET.get("grade", '')
        charge_choice = request.GET.get("charge", '')

        # 条件判断筛选课程
        # 年级筛选
        if grade_choice == "9" or grade_choice == '':
            course_1 = course_0
        else:
            course_1 = course_0.filter(grade_course=grade_choice)
        # 科目筛选
        if subject_choice == "0" or subject_choice == '':
            course_2 = course_1
        else:
            course_2 = course_1.filter(subject=subject_choice)
        # 时薪筛选
        if charge_choice == "1":
            course_3 = course_2.filter(charge__lte=30)
        elif charge_choice == "2":
            course_3 = course_2.filter(charge__range=[30, 50])
        elif charge_choice == "3":
            course_3 = course_2.filter(charge__range=[50, 70])
        elif charge_choice == "4":
            course_3 = course_2.filter(charge__range=[70, 100])
        elif charge_choice == "5":
            course_3 = course_2.filter(charge__gt=100)
        else:
            course_3 = course_2
        # 教师性别筛选
        if gender_choice == "0" or gender_choice == '':
            course_4 = course_3
        else:
            course_4 = []
            for course in course_3:
                if course.teacher.gender == gender_choice:
                    course_4 = course_4 + [course]

        # 展示课程向前端
        context = {'course': course_4}
        return render(request, 'filter.html', context)
    else:
        return HttpResponse("请使用GET请求数据")


# 增加课程
@login_required(login_url='/user/login/')
def increase_course(request):
    user = User.objects.get(id=request.user.id)
    if user.is_teacher == True:
        if request.method == "POST":
            if request.user != user:
                return HttpResponse("你没有权限修改此用户信息。")

            course_form = CourseForm(request.POST)
            this_teacher = Teacher.objects.get(teacher_user_id=request.user.id)
            if course_form.is_valid():
                new_course = course_form.save(commit=False)
                # 还要存一些表单给不了的数据
                new_course.teacher = this_teacher
                new_course.state_match = False
                new_course.save()
                return redirect("Course:detail_course", coursedetail_id=new_course.id)
            else:
                return HttpResponse("有字段输入不合要求")

        elif request.method == "GET":
            course_form = CourseForm()
            context = {'form': course_form}
            return render(request, 'Course/increase_course.html', context)
        else:
            return HttpResponse("请使用GET或POST请求数据")
    else:
        return HttpResponse("只有老师才能开设新课程哦")


# 学生进行课程申请
def match(request, coursedetail_id):
    course_applying = CourseDetail.objects.get(id=coursedetail_id)
    this_user = User.objects.get(id=request.user.id)
    # 虽然前端控制只有学生浏览课程详情页面时才有“申请”的按钮，但这里多一个判断更安全
    if this_user.is_student == True:
        # 多对多中间表加一个元组，下面this_user.student_profile使用了外键的related_name属性
        applicant = this_user.student_profile
        course_applying.student_applied.add(applicant)
        course_applying.save()
        return redirect('Course:manage_course')
    else:
        return HttpResponse("只有学生可以申请选课")
    return redirect('Course:detail_course', coursedetail_id=coursedetail_id)


# 同意申请
@login_required(login_url='/user/login/')
def agree_match(request, coursedetail_id):
    course_applying = CourseDetail.objects.get(id=coursedetail_id)
    selected_student = Student.objects.get(id=request.POST['choice'])
    course_applying.student_agreed = selected_student
    course_applying.state_match = True
    course_applying.save()
    return redirect('Course:manage_course')


# 课程详细内容
@login_required(login_url='/user/login/')
def detail_course(request, coursedetail_id):
    course = CourseDetail.objects.get(id=coursedetail_id)
    context = {'course': course, 'coursedetail_id': coursedetail_id}
    return render(request, 'Course/detail.html', context)


# 课程的删除
# 根据博客的教程，该功能还可以在安全性上进行一些改进
@login_required(login_url='/user/login/')
def delete_course(request, coursedetail_id):
    course = CourseDetail.objects.get(id=coursedetail_id)
    if course.state_match == 0:
        course.delete()
        return redirect('Course:manage_course')
    else:
        return HttpResponse("该课程已匹配完成，不可删除")


# 课程管理
# 学生和老师共同使用这个视图函数
@login_required(login_url='/user/login/')
def manage_course(request):
    # 通过request获得user对象
    user = request.user

    if user.is_teacher:
        # 查询匹配的课程
        course_match = user.teacher_profile.coursedetail_set.filter(state_match=True)
        # 反查询未匹配的课程
        course_unmatched = user.teacher_profile.coursedetail_set.filter(state_match=False)

        context = {'course_match': course_match, 'course_unmatched': course_unmatched}
        return render(request, 'Course/teacher_subject_detail.html', context)
    if user.is_student:

        course_match = user.student_profile.agreed_Student.filter(state_match=True)
        # 同时反查询和对课程进行过滤
        course_applying = user.student_profile.applied_Student.filter(state_match=False)
        # 这里做这个判断是为了解决 在评论过后直接定位到原来的tab窗口下
        if request.method == "POST":
            course = CourseDetail.objects.get(id=request.POST['course_id'])
            course.comment = request.POST['comment']
            course.save()
            context = {'course_match': course_match, 'course_applying': course_applying, 'flag': True}
        else:
            context = {'course_match': course_match, 'course_applying': course_applying, 'flag': False}

        return render(request, 'Course/student_subject_detail.html', context)
