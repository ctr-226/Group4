from django.test import TestCase
import datetime
from Course.models import CourseDetail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from User_Profile.forms import TeacherProfileForm, StudentProfileForm, UserRegisterForm, UserLoginForm
from User_Profile.models import Student, User, Teacher

from django.urls import reverse

# Create your tests here.

class UserModelTest(TestCase):
    # 测试基本的模型属性
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        new_user1 = User.objects.create_user(username='test_user_student', password='password_test', is_student=True)
        Student.objects.create(student_user=new_user1, mailbox="mail@gmail.com", phone='18238099856')
        new_user2 = User.objects.create_user(username='test_user_teacher', password='password_test', is_teacher=True)
        Teacher.objects.create(teacher_user=new_user2, name='test_user_teacher', mailbox="mail@gmail.com",
                               phone='18238099856')

    def test_name_label(self):
        student = Student.objects.get(id=1)
        label = student._meta.get_field('name').verbose_name
        self.assertEquals(label, '姓名')

    def test_name_length(self):
        student = Student.objects.get(id=1)
        label = student._meta.get_field('name').max_length
        self.assertEquals(label, 100)

    def test_age_label(self):
        student = Student.objects.get(id=1)
        label = student._meta.get_field('age').verbose_name
        self.assertEquals(label, '年龄')

    def test_gender_length(self):
        student = Student.objects.get(id=1)
        length = student._meta.get_field('gender').max_length
        self.assertEquals(length, 2)

    def test_grade_label(self):
        student = Student.objects.get(id=1)
        label = student._meta.get_field('grade').verbose_name
        self.assertEquals(label, '年级')

    def test_mail_label(self):
        student = Student.objects.get(id=1)
        label = student._meta.get_field('mailbox').verbose_name
        self.assertEquals(label, '个人邮箱')

    def test_phone_label(self):
        student = Student.objects.get(id=1)
        label = student._meta.get_field('phone').verbose_name
        self.assertEquals(label, '联系电话')

    def test_introduction_lable(self):
        student = Student.objects.get(id=1)
        label = student._meta.get_field('briefintroduction').verbose_name
        self.assertEquals(label, '教师信息')

    def test_introduction_text(self):
        student = Student.objects.get(id=1)
        label = student._meta.get_field('briefintroduction').help_text
        self.assertEquals(label, '个人简介，所在学校/学习情况等')

    def test_teacher(self):
        # user = User.objects.get(id=2)
        # teacher = user.teacher_profile
        teacher = Teacher.objects.get(id=1)
        self.assertEqual(teacher.name, 'test_user_teacher')


class UserLoginFormTest(TestCase):
    """测试登录表单字段是否符合预期"""

    def test_login_form_username_field_label(self):
        form = UserLoginForm()
        self.assertTrue(form.fields['username'].label == None or form.fields['username'].label == 'username')
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'password')
