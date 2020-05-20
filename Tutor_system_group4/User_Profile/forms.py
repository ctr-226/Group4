# 引入表单类
from django import forms
# 引入 User 模型 ，用户数据都存在这一模型对应数据库中
from django.contrib.auth.models import User
# 引入 Profile 模型
from .models import Student,Teacher
from .models import User
import re

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['age', 'gender', 'grade' , 'avatar']

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['age', 'gender', 'grade'  , 'avatar']

def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)

class UserRegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    user_attribute = forms.ChoiceField(choices=((0, '教员'), (1, '学员'),), required=True, label='选择属性')
    phone = forms.CharField(label='电话', max_length=12)

    # Use clean methods to define custom validation rules

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 4:
            raise forms.ValidationError("Your username must be at least 4 characters long.")
        elif len(username) > 50:
            raise forms.ValidationError("Your username is too long.")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError("Your username already exists.")
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 5:
            raise forms.ValidationError("Your password is too short.")
        elif len(password1) > 20:
            raise forms.ValidationError("Your password is too long.")

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password mismatch. Please enter again.")

        return password2


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
