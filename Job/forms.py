from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib import auth
from .models import *


class JobForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Job Title :"
        self.fields['company_name'].label = "Company name :"
        self.fields['description'].label = "Job description :"
        # self.fields['date'].label="date job"
        self.fields['workplace_type'].label = "Work Place Type :"
        self.fields['employment_type'].label = "Employments Type :"
        self.fields['experience'].label = "Job Experience :"
        self.fields['skills'].label = "Job Skils :"
        self.fields['location'].label = "Job Location :"
        self.fields['job_function'].label = "Job Function :"

        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'eg : Software Developer',
            }
        )
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': 'eg : Company Name',
            }
        )
        self.fields['description'].widget.attrs.update(
            {
                'placeholder': 'eg : Jod description',
            }
        )
        self.fields['workplace_type'].widget.attrs.update(
            {
                'placeholder': 'eg : On-site',
            }
        )
        self.fields['employment_type'].widget.attrs.update(
            {
                'placeholder': 'eg : Full time',
            }
        )
        self.fields['experience'].widget.attrs.update(
            {
                'placeholder': 'eg : Full Stack',
            }
        )
        self.fields['skills'].widget.attrs.update(
            {
                'placeholder': 'eg :Java',
            }
        )
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'eg :Lattika',
            }
        )
        self.fields['job_function'].widget.attrs.update(
            {
                'placeholder': 'eg :Build applications',
            }
        )

    class Meta:
        model = Job
        fields = ['title', 'company_name',
                  'description', 'workplace_type',
                  'employment_type', 'experience',
                  'skills', 'location', 'job_function', ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')

        if not job_type:
            raise forms.ValidationError("Service is required")
        return job_type

    def save(self, commit=True):
        job = super(JobForm, self).save(commit=False)

        if commit:
            job.save()
        return job


class JobApplyForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['job']


class JobEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Job Title :"
        self.fields['company_name'].label = "Company name :"
        self.fields['description'].label = "Job description :"
        # self.fields['date'].label="date job"
        self.fields['workplace_type'].label = "Work Place Type :"
        self.fields['employment_type'].label = "Employments Type :"
        self.fields['experience'].label = "Job Experience :"
        self.fields['skills'].label = "Job Skils :"
        self.fields['location'].label = "Job Location :"
        self.fields['job_function'].label = "Job Function :"

        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'eg : Software Developer',
            }
        )
        self.fields['company_name'].widget.attrs.update(
            {
                'placeholder': 'eg : Company Name',
            }
        )
        self.fields['description'].widget.attrs.update(
            {
                'placeholder': 'eg : Jod description',
            }
        )
        self.fields['workplace_type'].widget.attrs.update(
            {
                'placeholder': 'eg : On-site',
            }
        )
        self.fields['employment_type'].widget.attrs.update(
            {
                'placeholder': 'eg : Full time',
            }
        )
        self.fields['experience'].widget.attrs.update(
            {
                'placeholder': 'eg : Full Stack',
            }
        )
        self.fields['skills'].widget.attrs.update(
            {
                'placeholder': 'eg :Java',
            }
        )
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'eg :Lattika',
            }
        )
        self.fields['job_function'].widget.attrs.update(
            {
                'placeholder': 'eg :Build applications',
            }
        )

        class Meta:
            model = Job
        fields = ['title', 'company_name',
                  'description', 'workplace_type',
                  'employment_type', 'experience',
                  'skills', 'location', 'job_function', ]

        def clean_job_type(self):
            job_type = self.cleaned_data.get('job_type')

            if not job_type:
                raise forms.ValidationError("Service is required")
            return job_type

    def save(self, commit=True):
        job = super(JobEditForm, self).save(commit=False)

        if commit:
            job.save()
        return job
