# 引入path
from django.urls import path,include
from . import views

app_name = 'User_Profile'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('student_profile_update/',views.student_profile_update,name='student_profile_update'),
    path('teacher_profile_update/',views.teacher_profile_update,name='teacher_profile_update'),
]