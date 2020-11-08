from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeLoginForm, EmployeeRegisterForm
from django.utils.http import is_safe_url
from Employee.models import Employee




def emp_login_page(request):
	form = EmployeeLoginForm(request.POST or None)
	
	next_ = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_path = next_ or next_post
	if form.is_valid():
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			try:
				pass
			except:
				pass
			if is_safe_url(redirect_path, request.get_host()):
				return redirect(redirect_path)
			else:
				return redirect('/')
		else:
			...
	context = {
		'form':form
	}
	return render(request, "accounts/sign-in.html", context)



def emp_register_page(request):
	form = EmployeeRegisterForm(request.POST or None)
	if form.is_valid():
		emp_username = request.POST.get("emp_username")
		emp_email = request.POST.get("emp_email")
		emp_password = request.POST.get("emp_password")
		new_user = User.objects.create_user(emp_username, emp_email, emp_password)
		print(new_user)
		instance = Employee.objects.create(user=new_user)

		
	context = {
		"form":form
	}

	return render(request, "accounts/sign-in.html", context)
