from django import forms
from .models import Profile, JobApplication

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = '__all__'
