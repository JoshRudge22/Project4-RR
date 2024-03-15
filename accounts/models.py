from django.db import models

class Applying(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    cv = models.FileField(upload_to='cv_documents/')
    skills = models.TextField(blank=True, null=True)

class Hiring(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)

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