from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Job(models.Model):
    job_title = models.CharField(max_length=100)
    job_benefits = models.TextField()
    address = models.CharField(max_length=60)
    job_details = models.TextField()    
    job_requirements = models.TextField()
    interview_date = models.DateField(blank=True, null=True)
    available_times = models.ManyToManyField('AvailableTime', related_name='jobs')
    hired = models.BooleanField()

    def __str__(self):
        return self.job_title

class AvailableTime(models.Model):
    TIME_CHOICES = [
        ('10:00 - 11:00', '10:00 - 11:00'),
        ('11:00 - 12:00', '11:00 - 12:00'),
        ('12:00 - 13:00', '12:00 - 13:00'),
        ('13:00 - 14:00', '13:00 - 14:00'),
        ('14:00 - 15:00', '14:00 - 15:00'),
        ('15:00 - 16:00', '15:00 - 16:00'),
    ]
    time = models.CharField(max_length=20, choices=TIME_CHOICES)

    def __str__(self):
        return self.time

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    cv = models.FileField(upload_to='cv/', blank=True)


