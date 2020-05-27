from django.test import TestCase, Client, LiveServerTestCase
from .models import Teacher, Student, User, AbstractUser
from django.urls import reverse


class LoginViewTests(TestCase):

    def setUp(self):
        Teacher.objects.create(id=1, name='teacher1', age=20, gender='M', grade='1', mailbox='111@qq.com')
        Student.objects.create(id=1, name='teacher1', age=15, gender='F', grade='5', mailbox='111@qq.com')

    def test_login_with_right_user(self):
        """"""

# Create your tests here.
