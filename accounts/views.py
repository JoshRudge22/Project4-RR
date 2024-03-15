from django.shortcuts import render
from .forms import ApplyingForm, HiringForm, ContactForm

def home(request):
    return render(request, 'index.html')

def advertising(request):
    return render(request, 'advertising.html')

def hiring_form(request):
    if request.method == 'POST':
        form = HiringForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'New Job Application'
            message = f'Name: {form.cleaned_data["name"]}\nEmail: {form.cleaned_data["email"]}\n...'
            from_email = 'joshrudge@hotmail.com'
            to_email = ['rudgejosh@hotmail.com']
            send_mail(subject, message, from_email, to_email)
            return redirect('home')
    else:
        form = HiringForm()

    return render(request, 'hiring.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            subject = f"Contact Form Submission from {name}"
            message_body = f"Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\n\nMessage:\n{message}"
            send_mail(
                subject,
                message_body,
                'rudgejosh@hotmail.com',
                ['joshrudge@hotmail.com'], 
                fail_silently=False,
            )
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ContactUsForm()
    return render(request, 'contact.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            subject = f"Contact Form Submission from {name}"
            message_body = f"Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\n\nMessage:\n{message}"
            send_mail(
                subject,
                message_body,
                'rudgejosh@hotmail.com',
                ['joshrudge@hotmail.com'], 
                fail_silently=False,
            )
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})