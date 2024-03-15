from django.urls import path
from .views import home, contact_view, advertising
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('advertising/', advertising, name='advertising'),
    path('contact/', contact_view, name='contact'),
]