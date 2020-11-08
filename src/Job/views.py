try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass

from django.shortcuts import render,  get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from .forms import JobPostForm
from .models import Job
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.contenttypes.models import ContentType



def job_post(request):		
	form = JobPostForm(request.POST or None)
	user = get_object_or_404(User,username__iexact=request.user)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		print(instance.user)
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
	if instance.salaray == None:
		instance.salaray = "negotiable"
	if instance.employment_status =="f":
		instance.employment_status = "Full Time"
	elif instance.employment_status =="p":
		instance.employment_status = "Part Time"
	elif instance.employment_status =="r":
		instance.employment_status = "Remote"

		
	share_string = quote_plus(instance.position)
	content_type = ContentType.objects.get_for_model(Job)
	obj_id = instance.id
	context = {
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "job/job_details.html", context)