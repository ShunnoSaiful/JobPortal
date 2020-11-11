from django import forms
from pagedown.widgets import PagedownWidget, AdminPagedownWidget
from .models import Job


class JobPostForm(forms.ModelForm):
    application_deadline  = forms.DateField(widget=forms.SelectDateWidget, input_formats=['%d/%m/%Y'], required=False)
    job_context           = forms.CharField(widget=PagedownWidget(), required=False)
    job_responsibility    = forms.CharField(widget=PagedownWidget(), required=False)
    educational_req       = forms.CharField(widget=PagedownWidget(), required=False)
    experience_req        = forms.CharField(widget=PagedownWidget(), required=False)
    additional_req        = forms.CharField(widget=PagedownWidget(), required=False)
    compensation          = forms.CharField(widget=PagedownWidget(), required=False)
    application_procedure = forms.CharField(widget=PagedownWidget(), required=False)
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