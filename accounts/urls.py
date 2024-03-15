from django.urls import path
from .views import home, contact_view, advertising, hiring_form
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('advertising/', advertising, name='advertising'),
    path('contact/', contact_view, name='contact'),
    path('hiring/', hiring_form, name='hiring'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]