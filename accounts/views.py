from django.shortcuts import render, redirect  
from django.contrib import messages
from .forms import ApplyingForm, HiringForm, ContactForm
from .models import ContactUsForm, Hiring

def home(request):
    return render(request, 'index.html')

def advertising(request):
    return render(request, 'advertising.html')

def hiring_form(request):
    if request.method == 'POST':
        form = HiringForm(request.POST, request.FILES)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            job_description = form.cleaned_data['job_description']
            job_doc = form.cleaned_data['job_doc']
            contact_form_data = Hiring.objects.create(
                company_name=company_name,
                email=email,
                phone_number=phone_number,
                job_description=job_description,
                job_doc=job_doc,
            )
            return redirect('home')
    else:
        form = HiringForm()

    return render(request, 'hiring.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            best_time_to_contact = form.cleaned_data['best_time_to_contact']
            contact_form_data = ContactUsForm.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                message=message,
                best_time_to_contact=best_time_to_contact
            )
            
            messages.success(request, 'Your form was submitted successfully!')
            
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

