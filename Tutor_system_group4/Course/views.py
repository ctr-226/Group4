from django.shortcuts import render
from User_Profile.models import Student, Teacher, User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .models import CourseDetail
from django.contrib.auth.decorators import login_required


# Create your views here.
# 课程申请匹配
def match(request):
    return None


# 增加课程
def increase_course(request):
    return None


# 同意申请
def agree_match(request, coursedetail_id):
    course_applying = CourseDetail.objects.get(id=coursedetail_id)
    selected_student = Student.objects.get(id=request.POST['choice'])
    course_applying.student_agreed = selected_student
    course_applying.state_match = True
    course_applying.save()
    return redirect('Course:manage_course')


# 课程详细内容

def detail_course(request, id):
    course = CourseDetail.objects.get(id=id)
    context = {'course': course}
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
                # course_applying.append(course)
                # student_applying.append(course.student_applied.all())
                course_list[course] = course.student_applied.all()
        context = {'course_match': course_match, 'course_unmatched': course_unmatched,
                   'course_list': course_list}
        return render(request, 'Course/teacher_subject_detail.html', context)
    if user.is_student:
        course_match = Student.objects.get(id=ID).coursedetail_set.filter(state_match=True)
        course_applying = Student.objects.get(id=ID).applied_Student.all()
        context = {'course_match': course_match, 'course_applying': course_applying}
        return render(request, 'Course/student_subject_detail.html', context)
