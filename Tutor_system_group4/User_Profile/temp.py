@login_required(login_url='/user/login/')
def profile_update(request,id):
	user = User.objects.get(id=id)
	if request.method == 'POST':
		if request.user != user:
			return HttpResponse("你没有权限修改此用户信息。")
		if user.is_student == True:
			student_profile = Student.objects.get(student_user_id=id)
			student_form = StudentProfileForm(request.POST)
			if student_form.is_valid():
				profile_cd = student_form.cleaned_data
				student_profile.age = profile_cd['age']
				student_profile.gender = profile_cd['gender']
				student_profile.grade = profile_cd['grade']
				student_profile.save()
				return redirect("User_Profile:profile_update", id=id)
			else:
				return HttpResponse("注册表单输入有误。请重新输入")

		elif user.is_teacher == True:
			teacher_profile = Teacher.objects.get(student_user_id=id)
			teacher_form = TeacherProfileForm(request.POST)
			if teacher_form.is_valid():
				profile_cd = teacher_form.cleaned_data
				teacher_profile.age = profile_cd['age']
				teacher_profile.gender = profile_cd['gender']
				teacher_profile.grade = profile_cd['grade']
				teacher_profile.save()
				return redirect("User_Profile:profile_update", id=id)
			else:
				return HttpResponse("注册表单输入有误。请重新输入")
		else:
			return HttpResponse("请明确用户身份")
	
	elif request.method == 'GET':
		if user.is_student == True:
			student_form = StudentProfileForm()
			context = {'form': student_form}
			return render(request, 'User_Profile/student_profile_update.html', context)
		elif user.is_teacher == True:
			teacher_form = TeacherProfileForm()
			context = {'form': teacher_form}
			return render(request, 'User_Profile/teacher_profile_update.html', context)
	else:
		return HttpResponse("请使用GET或POST请求数据")