from django.db import models


class ContactUsForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    best_time_to_contact = models.CharField(max_length=10, choices=[
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    ], blank=True)
    
    def __str__(self):
        return self.name