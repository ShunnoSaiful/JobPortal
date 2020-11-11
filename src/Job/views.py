try:
    from urllib.parse import quote_plus
except: 
    pass

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,  get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from .forms import JobPostForm
from .models import Job
from django.db.models import Q
from django.contrib.auth.models import User
from Company.models import Company
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.contenttypes.models import ContentType


@login_required 
def job_post(request):		
	form = JobPostForm(request.POST or None)
	user = get_object_or_404(User,username__iexact=request.user)
	print(user)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "job/job_post.html", context)


def job_list(request):
	queryset_list = Job.objects.active() #.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Job.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(position__icontains=query)|
				Q(job_context__icontains=query)|
				Q(job_responsibility__icontains=query) |
				Q(experience_req__icontains=query) |
				Q(employment_status__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset, 
		"page_request_var": page_request_var,
	}
	return render(request, "job/jobs.html", context)



def job_details(request, slug=None):
	instance = get_object_or_404(Job, slug=slug)
	print(instance.company)
	instance.count=instance.count+1
	print(instance.count)
	instance.save()
	if instance.salaray == None:
		instance.salaray = "negotiable"
	if instance.employment_status =="f":
		instance.employment_status = "Full Time"
	elif instance.employment_status =="p":
		instance.employment_status = "Part Time"
	elif instance.employment_status =="r":
		instance.employment_status = "Remote"

		
	obj_id = instance.id
	context = {
		"instance": instance,
	}
	return render(request, "job/job_details.html", context)