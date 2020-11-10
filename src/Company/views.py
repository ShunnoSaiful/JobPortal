from django.shortcuts import render
from .models import Company, Address

# Create your views here.



def view_profile(request, slug=None):
	instance = get_object_or_404(Company, slug=slug)
	context = {
		"instance": instance,
	}
	return render(request, "employee/company-profile.html.html", context)