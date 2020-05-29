from django.test import TestCase
import datetime
from User_Profile.models import Student, User, Teacher
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Course.forms import CourseForm
from Course.models import CourseDetail
from django.utils import timezone

class CourseModelTest(TestCase):
    # 测试基本的模型属性
    @classmethod
    def setUp(self):
        # 设置好两个学生账户和一个老师账户
        new_user = User.objects.create_user(username='test_user_student', password='password_test1', is_student=True)
        student1 = Student.objects.create(student_user=new_user, mailbox="mail@gmail.com", phone='18238099856')
        new_user1 = User.objects.create_user(username='test_user_student1', password='password_test1', is_student=True)
        student2 = Student.objects.create(student_user=new_user1, mailbox="mail@gmail.com", phone='18238099856')
        new_user2 = User.objects.create_user(username='test_user_teacher', password='password_test2', is_teacher=True)
        teacher1 = Teacher.objects.create(teacher_user=new_user2, name='test_user_teacher', mailbox="mail@gmail.com",
                                          phone='18238099856')
        course = CourseDetail.objects.create(teacher=teacher1, nick_name='class1', grade_course='1', subject='zh',
                                             introduction='hello', charge=1, time_set=timezone.now(), state_match=0)
        course.student_applied.add(student1, student2)


    def test_nick_name_label(self):
        course = CourseDetail.objects.get(id=1)
        label = course._meta.get_field('nick_name').verbose_name
        self.assertEquals(label,'课程名称')
    
    def test_nick_name_length(self):
        course = CourseDetail.objects.get(id=1)
        label = course._meta.get_field('nick_name').max_length
        self.assertEquals(label,50)

    def test_grade_course_label(self):
        course = CourseDetail.objects.get(id=1)
        label = course._meta.get_field('grade_course').verbose_name
        self.assertEquals(label,"学生年级")

    def test_subject_label(self):
        course = CourseDetail.objects.get(id=1)
        label = course._meta.get_field('subject').verbose_name
        self.assertEquals(label,"科目")

    def test_introduction_label(self):
        course = CourseDetail.objects.get(id=1)
        label = course._meta.get_field('introduction').verbose_name
        self.assertEquals(label,"简介")

    def test_introduction_length(self):
        course = CourseDetail.objects.get(id=1)
        label = course._meta.get_field('introduction').max_length
        self.assertEquals(label,150)
    
    def test_charge_label(self):
        course = CourseDetail.objects.get(id=1)
        label = course._meta.get_field('charge').verbose_name
        self.assertEquals(label,"课程收费")

    def test_comment_label(self):
        course = CourseDetail.objects.get(id=1)
        label = course._meta.get_field('comment').verbose_name
        self.assertEquals(label,"评论")

    def test_comment_length(self):
        course = CourseDetail.objects.get(id=1)
        label = course._meta.get_field('comment').max_length
        self.assertEquals(label,100)

    def test_student_agreed_label(self):
        course = CourseDetail.objects.get(id=1)
        label = course._meta.get_field('student_agreed').verbose_name
        self.assertEquals(label,"成功匹配")
    
    def test_student_applied_label(self):
        course = CourseDetail.objects.get(id=1)
        label = course._meta.get_field('student_applied').verbose_name
        self.assertEquals(label,"申请学员")
    
    



# Create your tests here.
