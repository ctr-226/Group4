from django.test import TestCase
import datetime
from User_Profile.models import Student, User, Teacher
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Course.forms import CourseForm
from Course.models import CourseDetail


class CourseModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        new_user = User.objects.create_user(username='test_user_teacher', password='password_test', is_teacher=True)
        Teacher.objects.create(teacher_user=new_user, name='test_user_teacher', mailbox="mail@gmail.com",
                               phone='18238099856')
        teacher = Teacher.objects.get(id=1)
        Course.objects.create(teacehr=teacher,nick_name='teat_class',grade_course='8',subject='zh')
    
    def test_nick_name_label(self):
        course = Course.objects.get(id=1)
        label = course._meta.get_field('nick_name').verbose_name
        self.assertEquals(label,'课程名称')

    def test_nick_name_label(self):
        course = Course.objects.get(id=1)
        label = course._meta.get_field('nick_name').max_length
        self.assertEquals(label,50)

    def test_grade_course_label(self):
        course = Course.objects.get(id=1)
        label = course._meta.get_field('grade_course').verbose_name
        self.assertEquals(label,"学生年级")

    def test_subject_label(self):
        course = Course.objects.get(id=1)
        label = course._meta.get_field('subject').verbose_name
        self.assertEquals(label,"科目")

    def test_introduction_label(self):
        course = Course.objects.get(id=1)
        label = course._meta.get_field('introduction').verbose_name
        self.assertEquals(label,"简介")

    def test_introduction_label(self):
        course = Course.objects.get(id=1)
        label = course._meta.get_field('introduction').max_length
        self.assertEquals(label,150)
    
    def test_charge_label(self):
        course = Course.objects.get(id=1)
        label = course._meta.get_field('charge').verbose_name
        self.assertEquals(label,"课程收费")

    def test_comment_label(self):
        course = Course.objects.get(id=1)
        label = course._meta.get_field('comment').verbose_name
        self.assertEquals(label,"评论")

    def test_comment_label(self):
        course = Course.objects.get(id=1)
        label = course._meta.get_field('comment').max_length
        self.assertEquals(label,100)

    def test_student_agreed_label(self):
        course = Course.objects.get(id=1)
        label = course._meta.get_field('student_agreed').verbose_name
        self.assertEquals(label,"成功匹配")
    
    def test_student_applied_label(self):
        course = Course.objects.get(id=1)
        label = course._meta.get_field('student_applied').verbose_name
        self.assertEquals(label,"申请学员")
    
    



# Create your tests here.
