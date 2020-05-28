from django.test import TestCase
import datetime
from Course.models import CourseDetail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, resolve
from User_Profile.models import Teacher, Student, User
from Course.views import manage_course
from django.utils import timezone


class ManageCourseTests(TestCase):
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

        self.url = reverse('Course:manage_course')

    def test_manage_get_status(self):
        # 测试返回status
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_manage_url_resolves_view(self):
        # 测试解析函数
        view = resolve('/course/manage_course/')
        self.assertEqual(view.func, manage_course)

    def test_redirect_if_not_logged_in(self):
        # 测试未登录的时候重定向
        resp = self.client.get(self.url)
        self.assertRedirects(resp, '/user/login/?next=/course/manage_course/')

    def test_logged_in_users_teacher_correct(self):
        # 测试教员登录之后 查看课程的操作
        login = self.client.login(username='test_user_teacher', password='password_test2')
        resp = self.client.get(self.url)

        # 查看基本的表单等csrf
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'csrfmiddlewaretoken')
        self.assertEqual(str(resp.context['user']), 'test_user_teacher')

        course_unmatched = resp.context['course_unmatched']
        course = course_unmatched[0]
        self.assertEqual(course.nick_name, 'class1')
        # Check we used correct template
        self.assertTemplateUsed(resp, 'Course/teacher_subject_detail.html')

    def test_logged_in_users_student_correct(self):
        login = self.client.login(username='test_user_student', password='password_test1')

        resp = self.client.get(self.url)

        #
        self.assertEqual(str(resp.context['user']), 'test_user_student')
        self.assertEqual(resp.status_code, 200)
        course_applying = resp.context['course_applying']
        course = course_applying[0]
        self.assertEqual(course.nick_name, 'class1')
        # 测试 correct template
        self.assertTemplateUsed(resp, 'Course/student_subject_detail.html')

    def test_manage_teacher_post(self):
        # 测试模拟同意某个同学申请的操作
        login = self.client.login(username='test_user_teacher', password='password_test2')
        # 这个可以换成其他的数字
        data = {
            'choice': '2'
        }
        resp = self.client.post(reverse('Course:agree_match', kwargs={'coursedetail_id': '1'}), data)
        resp1 = self.client.get(self.url)
        course_match = resp1.context['course_match']
        course = course_match[0]
        self.assertEqual(course.nick_name, 'class1')
        self.assertRedirects(resp, self.url)
