from django import forms
from pagedown.widgets import PagedownWidget

from .models import Job


class JobPostForm(forms.ModelForm):
    application_deadline  = forms.DateField(widget=forms.SelectDateWidget)
    job_context           = forms.CharField(widget=PagedownWidget())
    job_responsibility    = forms.CharField(widget=PagedownWidget())
    educational_req       = forms.CharField(widget=PagedownWidget())
    experience_req        = forms.CharField(widget=PagedownWidget())
    additional_req        = forms.CharField(widget=PagedownWidget())
    compensation          = forms.CharField(widget=PagedownWidget())
    application_procedure = forms.CharField(widget=PagedownWidget())
    class Meta:
        model = Job
        fields = [
            "position",
            "job_context",
            "job_responsibility",
            "employment_status",
            "educational_req",
            "experience_req",
            "additional_req",
            "job_location",
            "salaray",
            "compensation",
            "application_deadline",
            "application_procedure",
        ]