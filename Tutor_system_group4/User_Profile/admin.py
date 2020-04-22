from django.contrib import admin

# 导入Teacher,Student
from .models import Teacher, Student, User

# 注册Teacher,Student到admin中
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(User)
