from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from Job.forms import JobPostForm	

# Create your views here.
def home(request): 
	return render(request, "index.html", {})
