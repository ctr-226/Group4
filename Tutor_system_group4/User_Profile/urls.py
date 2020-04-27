# 引入path
from django.urls import path, include
from . import views

app_name = 'User_Profile'
urlpatterns = [
	path('login/', views.user_login, name='login'),
	path('logout/', views.user_logout, name='logout'),
	path('register/', views.register, name='register'),
	path('profile_update/<int:id>/', views.profile_update, name='profile_update'),
]
