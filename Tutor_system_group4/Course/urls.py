from django.urls import path, include
from . import views

app_name = 'Course'
urlpatterns = [
    path('match/<int:coursedetail_id>/', views.match, name='match'),
    path('agree_match/<int:coursedetail_id>/', views.agree_match, name='agree_match'),
    path('increase_course/', views.increase_course, name='increase_course'),
    path('detail_course/<int:coursedetail_id>/', views.detail_course, name='detail_course'),
    path('manage_course/', views.manage_course, name='manage_course'),
]
