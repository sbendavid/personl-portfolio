from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name="home"),
    path('resume', views.resume, name="resume"),
    path('contact', views.contact, name="contact"),
    path('contact/success/', views.contact_success, name='contact_success'),
]