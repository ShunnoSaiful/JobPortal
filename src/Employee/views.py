from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from .models import Portfulio, Address, SocialLink, Employee, FollowRequest
from Job.models import Job

# Create your views here.
def home(request, id=None):
	queryset_list = Job.objects.all()
	instance = get_object_or_404(Employee, id=1)
	print(instance.emp_profile_image.url)
	context = {
		"instance": instance,
		"object": queryset_list,
	}
	return render(request, "index.html", context)


def view_profile(request, id=None):
	instance = get_object_or_404(Employee, id=1)
	context = {
		"instance": instance,
	}
	return render(request, "employee/profiles.html", context)