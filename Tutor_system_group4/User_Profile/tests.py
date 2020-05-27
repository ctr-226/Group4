from django.test import TestCase
from django.urls import reverse

from .models import Teacher, Student, User
from .forms import UserRegisterForm, UserLoginForm, StudentProfileForm, TeacherProfileForm

# Create your tests here.

class StudentProfileViewTests(TestCase):
    def setUp(self):
        #这里新建user元组对应的id应该是默认的1
        self.user = User.objects.create_user(username='lhy', password='123456', is_student=True)
        self.student = Student.objects.create(student_user=self.user, name='lhy', mailbox='1971905576@qq.com', phone='13697112122')
        
    def test_csrf(self):
        url = reverse('student_profile_update', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    #def test_contains_form(self):


#class TeacherProfileViewTests(TestCase):
    #def

