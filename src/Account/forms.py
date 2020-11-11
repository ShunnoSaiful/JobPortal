from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from Employee.models import Employee


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



class EmployeeRegisterForm(forms.Form):
	emp_username = forms.CharField(max_length=100, widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'placeholder':'Username'
		}))
	emp_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
		attrs={
		'class':'form-control',
		'placeholder':'Repeat Password'
		}))
	
	emp_email = forms.EmailField(max_length=100, widget=forms.EmailInput(
		attrs={
		'class':'form-control',
		'placeholder':'Email'
		}))
	emp_password = forms.CharField(max_length=100, widget=forms.PasswordInput(
		attrs={
		'class':'form-control',
		'placeholder':'Password'
		}))

	def clean_username(self):
		username = self.cleaned_data.get("emp_username")
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username already taken")
		return username

	def clean_email(self):
		email = self.cleaned_data.get("emp_email")
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("E-mail already taken")
		return email


	def clean_password2(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("emp_password")
		password2 = self.cleaned_data.get("emp_password2")
		if password2 != password:
			raise forms.ValidationError("Password doesn't match")
		return data


