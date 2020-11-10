from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from .models import Portfulio, Address, SocialLink, Employee, FollowRequest
from Job.models import Job
from Company.models import Company

# Create your views here.
def home(request):
	queryset_list = Job.objects.all().order_by('-count')
	user = request.user
	instance = Employee.objects.get(user=request.user)
	employee = Employee.objects.all()
	company  = Company.objects.all()
	print(instance)
	context = {
		"instance": instance,
		"object": queryset_list,
		"employee": employee,
		"company": company,
	}
	return render(request, "index.html", context)


def view_profile(request, slug=None):
	instance = get_object_or_404(Employee, slug=slug)
	context = {
		"instance": instance,
	}
	return render(request, "employee/user-profile.html", context)