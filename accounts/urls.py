from django.urls import path
from .views import home, contact_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact_view, name='contact'),
]