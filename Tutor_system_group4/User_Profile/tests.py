from django.test import TestCase
import datetime
from Course.models import CourseDetail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TeacherProfileForm, StudentProfileForm, UserRegisterForm, UserLoginForm
from .models import Student, User, Teacher


# Create your tests here.


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        new_user1 = User.objects.create_user(username='test_user_student', password='password_test', is_student=True)
        Student.objects.create(student_user=new_user1, mailbox="mail@gmail.com", phone='18238099856')

    def test_name_label(self):
        student = Student.objects.get(id=1)
        label = student._meta.get_field('name').verbose_name
        self.assertEquals(label, '姓名')

    def test_name_length(self):
        student = Student.objects.get(id=1)
        label = student._meta.get_field('name').max_length
        self.assertEquals(label, 100)


class UserRegisterFormTest(TestCase):
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
