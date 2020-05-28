from django.test import TestCase
from django.test.client import Client
import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect

from User_Profile.forms import TeacherProfileForm, StudentProfileForm, UserRegisterForm, UserLoginForm
from User_Profile.models import Student, User, Teacher

from django.urls import reverse

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