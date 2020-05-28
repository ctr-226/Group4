from django.test import TestCase, Client, LiveServerTestCase
from .models import Teacher, Student, User, AbstractUser
from django.urls import reverse
from .forms import UserLoginForm


class UserLoginFormTest(TestCase):
    """测试登录表单字段是否符合预期"""

    def test_login_form_username_field_label(self):
        form = UserLoginForm()
        self.assertTrue(form.fields['username'].label == None or form.fields['username'].label == 'username')
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'password')


# py manage.py test User_Profile
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

    def test_login(self):
        response = self.client.get(reverse('User_Profile:login'))
        login = self.client.login(username='teacher1', password="123456")
        self.assertTrue(login)

        # print(response.context)
# Create your tests here.
#py manage.py test User_Profile
