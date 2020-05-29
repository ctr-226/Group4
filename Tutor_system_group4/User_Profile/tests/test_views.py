from django.test.client import Client
from django.test import TestCase, LiveServerTestCase, Client
import datetime
from Course.models import CourseDetail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, resolve
from User_Profile.forms import UserLoginForm, UserRegisterForm, StudentProfileForm, TeacherProfileForm
from User_Profile.models import Teacher, Student, User
from User_Profile.views import register
#自己或他人查看个人信息页面视图函数的测试
class StudentProfileFormTests(TestCase):
    def setUp(self):
        # 这里新建user元组对应的id应该是默认的1
        self.client = Client()
        self.user1 = User.objects.create_user(username='lhy', password='123456', is_student=True)
        self.student1 = Student.objects.create(student_user=self.user1, name='lhy', mailbox='1971905576@qq.com', phone='13697112122')
        self.user2 = User.objects.create_user(username='tzx', password='123456', is_student=True)
        self.student2 = Student.objects.create(student_user=self.user2, name='tzx', mailbox='1971905577@qq.com', phone='13697112123')
        #self.client.login(username='lhy', password='123456')

    def test_view_url_exists_visited_by_self(self): 
        self.client.login(username='lhy', password='123456')
        id = self.student1.id
        url = reverse('User_Profile:student_profile_update', kwargs={'id': id})
        resp = self.client.get(url) 
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'User_Profile/student_profile_update.html')
        self.assertTrue('student_profile' in resp.context)
        self.assertTrue('form' in resp.context)

    def test_view_url_exists_visited_by_others(self): 
        self.client.login(username='tzx', password='123456')
        id = self.student1.id
        url = reverse('User_Profile:student_profile_update', kwargs={'id': id})
        resp = self.client.get(url) 
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'User_Profile/student_profile_update.html')
        self.assertTrue('student_profile' in resp.context)
        self.assertTrue('form' in resp.context)

#class TeacherProfileFormTests(TestCase):
# 由于学生和老师两个个人信息视图函数基本一致，此处老师个人信息表单的测试可以略去



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


class LoginViewTests(LiveServerTestCase):
    """测试登录函数"""

    def setUp(self):
        test_user1 = User.objects.create(id=1, username='teacher1')
        test_user1.set_password('123456')
        test_user1.save()
        # Student.objects.create(id=1, name='teacher1', age=15, gender='F', grade='5', mailbox='111@qq.com')
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/user/login/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('User_Profile:login'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('User_Profile:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'User_Profile/login.html')

    def test_login_with_right_user(self):
        response = self.client.get(reverse('User_Profile:login'))
        login = self.client.login(username='teacher1', password="123456")
        self.assertTrue(login)

    def test_login_with_wrong_user(self):
        response = self.client.get(reverse('User_Profile:login'))
        login = self.client.login(username='teacher1', password="1234567")
        self.assertFalse(login)
