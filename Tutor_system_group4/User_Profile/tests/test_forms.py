from django.test import TestCase
import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect

from User_Profile.forms import TeacherProfileForm, StudentProfileForm, UserRegisterForm, UserLoginForm
from User_Profile.models import Student, User, Teacher

from django.urls import reverse

class StudentProfileFormTests(TestCase):

    #对于模型表单，表单字段的label属性根据模型字段的verbose_name属性设置，并将第一个字母大写。
    def test_name_field(self):
        form = StudentProfileForm()
        label = form.fields['name'].label
        max_length = form.fields['name'].max_length
        self.assertTrue(label == None or label == '姓名')
        self.assertEqual(max_length, 100)

    def test_age_field_label(self):
        form = StudentProfileForm()
        label = form.fields['age'].label
        self.assertTrue(label == None or label == '年龄')

    def test_gender_field_label(self):
        form = StudentProfileForm()
        label = form.fields['gender'].label
        self.assertTrue(label == None or label == '性别')

    def test_grade_field_label(self):
        form = StudentProfileForm()
        label = form.fields['grade'].label
        self.assertTrue(label == None or label == '年级')

    def test_phone_field(self):
        form = StudentProfileForm()
        label = form.fields['phone'].label
        max_length = form.fields['phone'].max_length
        self.assertTrue(label == None or label == '联系电话')
        self.assertEqual(max_length, 12)

    def test_mailbox_field_label(self):
        form = StudentProfileForm()
        label = form.fields['mailbox'].label
        self.assertTrue(label == None or label == '个人邮箱')

    def test_avatar_field_label(self):
        form = StudentProfileForm()
        label = form.fields['avatar'].label
        self.assertTrue(label == None or label == '头像')

    def test_briefintroduction_field_label(self):
        form = StudentProfileForm()
        label = form.fields['briefintroduction'].label
        max_length = form.fields['briefintroduction'].max_length
        self.assertTrue(label == None or label == '学生信息')
        self.assertEqual(max_length, 100)

# class TeacherProfileFormTests(TestCase):
# 由于学生和老师两个表单基本一致，此处老师个人信息表单的测试就可以略去


class UserRegisterFormTest(TestCase):
    def test_username_field_label(self):
        form = UserRegisterForm()
        label = form.fields['username'].label
        self.assertEqual(label, 'Username')

    def test_email_field_label(self):
        form = UserRegisterForm()
        label = form.fields['email'].label
        self.assertEqual(label, 'Email')

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