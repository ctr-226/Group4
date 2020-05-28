from django.test import TestCase
import datetime
from User_Profile.models import Student, User ,Teacher
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Course.forms import CourseForm
from Course.models import CourseDetail




# Create your tests here.
