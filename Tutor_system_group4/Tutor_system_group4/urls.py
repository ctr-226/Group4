"""Tutor_system_group4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Course import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('User_Profile.urls'), name='user'),
    path('course/', include('Course.urls'), name='course'),
<<<<<<< HEAD
    path('', views.index, name='index'),
=======
    path('index/', views.index, name='index'),
    # path('filter/', views.filter, name='filter'),
>>>>>>> 61638aef03548b0d7230e2f34c1fc83c32076bf4
    path('index2/', views.index2, name='index2'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
