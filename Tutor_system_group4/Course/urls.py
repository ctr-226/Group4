from django.urls import path,include
from . import views

app_name = 'Course'
urlpatterns = [
    path('increase_course/<int:teacher_id>/', views.increase_course, name='increase_course'),
]