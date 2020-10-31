from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from Employee.models import Employee
User = get_user_model()


class EmployeeLoginForm(forms.Form):
	username = forms.CharField(max_length=100, widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'placeholder':'Username'
		}))
	password = forms.CharField(max_length=100, widget=forms.PasswordInput(
		attrs={
		'class':'form-control',
		'placeholder':'Password'
		}))


	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)
		if not qs.exists():
			raise forms.ValidationError("Username is not valid")
		return username

	def clean_password(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		if not user :
			raise forms.ValidationError("Password is not correct. Please enter valid one")
		return user



class EmployeeRegisterForm(forms.ModelForm):
	password2 = forms.CharField(
		widget=forms.PasswordInput(
		attrs={
		'class':'form-control',
		'placeholder':'Confirm Password'
		}))
	class Meta:
		model = Employee
		fields = [
			"emp_first_name",
			"emp_last_name",
			"emp_username",
			"emp_email",
			"emp_password",
			"password2"
		]


	def clean_username(self):
		emp_username = self.cleaned_data.get("emp_username")
		qs = User.objects.filter(emp_username=emp_username)
		if qs.exists():
			raise forms.ValidationError("Username already taken")
		return emp_username

	def clean_email(self):
		emp_email = self.cleaned_data.get("emp_email")
		qs = User.objects.filter(emp_email=emp_email)
		if qs.exists():
			raise forms.ValidationError("E-mail already taken")
		return emp_email


	def clean_password2(self):
		data = self.cleaned_data
		emp_password = self.cleaned_data.get("emp_password")
		password2 = self.cleaned_data.get("password2")
		if password2 != emp_password:
			raise forms.ValidationError("Password doesn't match")
		return data


