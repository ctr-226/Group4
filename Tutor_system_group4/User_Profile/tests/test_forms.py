from django.test import TestCase
import datetime
from Course.models import CourseDetail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from User_Profile.forms import UserLoginForm, UserRegisterForm, StudentProfileForm, TeacherProfileForm
from User_Profile.models import Teacher, Student, User

from django.urls import reverse


class StudentProfileViewTests(TestCase):
    def setUp(self):
        # 这里新建user元组对应的id应该是默认的1
        self.user = User.objects.create_user(username='lhy', password='123456', is_student=True)
        self.student = Student.objects.create(student_user=self.user, name='lhy', mailbox='1971905576@qq.com',
                                              phone='13697112122')

    def test_csrf(self):
        url = reverse('student_profile_update', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    # def test_contains_form(self):


# class TeacherProfileViewTests(TestCase):
# def

class UserRegisterFormTest(TestCase):
    # 测试基本的注册表单属性
    def test_username_field_label(self):
        form = UserRegisterForm()
        label = form.fields['username'].label
        self.assertEqual(label, 'Username')

    def test_email_field_label(self):
        form = UserRegisterForm()
        label = form.fields['email'].label
        self.assertEqual(label, 'email')

    def test_user_attribute_required(self):
        form = UserRegisterForm()
        required = form.fields['user_attribute'].required
        self.assertEqual(required, True)

    def test_phone(self):
        form = UserRegisterForm()
        label = form.fields['phone'].label
        max_length = form.fields['phone'].max_length
        self.assertEqual(label, '电话')
        self.assertEqual(max_length, 12)
