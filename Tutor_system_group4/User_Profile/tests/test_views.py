from django.test import TestCase
import datetime
from Course.models import CourseDetail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, resolve
from User_Profile.forms import UserLoginForm, UserRegisterForm, StudentProfileForm, TeacherProfileForm
from User_Profile.models import Teacher, Student, User
from User_Profile.views import register


class RegisterView(TestCase):
    # 测试 表单的基本属性
    def setUp(self):
        url = reverse('User_Profile:register')
        self.response = self.client.get(url)

    def test_register_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_register_url_resolves_view(self):
        view = resolve('/user/register/')
        self.assertEqual(view.func, register)

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserRegisterForm)

    def test_form_inputs(self):
        self.assertContains(self.response, '<input', 6)
        self.assertContains(self.response, 'type="text"', 2)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)


class SuccessStudentRegisterTests(TestCase):
    # 测试成功注册学员的操作
    def setUp(self):
        # 创建数据
        url = reverse('User_Profile:register')
        data = {
            'username': 'john',
            'email': '3568312831@qq.com',
            'password1': '2020ppp',
            'password2': '2020ppp',
            'user_attribute': '1',
            'phone': '13265557889'
        }
        self.response = self.client.post(url, data)
        self.login_url = reverse('User_Profile:login')

    def test_redirection(self):
        self.assertRedirects(self.response, self.login_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_student_right(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.is_student, True)


class SuccessTeacherRegisterTests(TestCase):
    # 测试成功注册教员的情况
    def setUp(self):
        url = reverse('User_Profile:register')
        data = {
            'username': 'john',
            'email': '3568312831@qq.com',
            'password1': '2020ppp',
            'password2': '2020ppp',
            'user_attribute': '0',
            'phone': '13265557889'
        }
        self.response = self.client.post(url, data)
        self.login_url = reverse('User_Profile:login')

    def test_redirection(self):
        self.assertRedirects(self.response, self.login_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_teacher_right(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.is_teacher, True)


class InvalidRegisterTests(TestCase):
    # 测试没有成功注册的操作
    def setUp(self):
        url = reverse('User_Profile:register')
        self.response = self.client.post(url, {})

    def test_register_status_code(self):
        self.assertEqual(self.response.status_code, 200)
