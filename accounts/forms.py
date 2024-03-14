from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(label='Email', required=False)
    phone_number = forms.CharField(max_length=15, label='Phone Number', required=False)
    message = forms.CharField(widget=forms.Textarea, label='Message')
    BEST_TIME_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    ]
    best_time_to_contact = forms.ChoiceField(
        choices=BEST_TIME_CHOICES,
        label='Best Time to Contact',
        required=False,
    )