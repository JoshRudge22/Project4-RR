from django import forms
from .models import Applying, Hiring, ContactUsForm

class ApplyingForm(forms.ModelForm):
    class Meta:
        model = Applying
        fields = '__all__'
        widgets = {
            'skills': forms.TextInput(attrs={'placeholder': 'Anything you feel will make you stand out as a candidate.'})
        }

class HiringForm(forms.ModelForm):
    class Meta:
        model = Hiring
        fields = '__all__'
        widgets = {
            'job_description': forms.TextInput(attrs={'placeholder': 'Salary, Hours, Postion, Job Type, Address, Job Details and Job Requirements.'})
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUsForm
        fields = '__all__'