from django.test import TestCase
import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Course.forms import CourseForm, FilterForm
from Course.models import CourseDetail
from User_Profile.models import Student, User, Teacher

from django.urls import reverse

class CourseFormTests(TestCase):
    def test_nick_name_field(self):
        form = CourseForm()
        label = form.fields['nick_name'].label
        max_length = form.fields['nick_name'].max_length
        self.assertTrue(label == None or label == '课程名称')
        self.assertEqual(max_length, 50)

    def test_grade_course_field(self):
        form = CourseForm()
        label = form.fields['grade_course'].label
        self.assertTrue(label == None or label == '学生年级')

    def test_subject_field(self):
        form = CourseForm()
        label = form.fields['subject'].label
        self.assertTrue(label == None or label == '科目')

    def test_charge_field(self):
        form = CourseForm()
        label = form.fields['charge'].label
        self.assertTrue(label == None or label == '课程收费')

    def test_introduction_field(self):
        form = CourseForm()
        label = form.fields['introduction'].label
        max_length = form.fields['introduction'].max_length
        self.assertTrue(label == None or label == '简介')
        self.assertEqual(max_length, 150)