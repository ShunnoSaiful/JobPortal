from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .forms import JobPostForm


def job_post(request):		
	form = JobPostForm(request.POST or None)
	print(form)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return HttpResponseRedirect('Employee:home')
	context = {
		"form": form,
	}
	return render(request, "job/job_post.html", context)
