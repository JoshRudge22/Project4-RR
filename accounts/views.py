from django.shortcuts import render
from .forms import ContactForm

def home(request):
    return render(request, 'index.html')

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