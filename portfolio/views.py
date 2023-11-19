from http.client import HTTPResponse
from django.shortcuts import render
from .models import Project, Contact
from .forms import ContactForm
from django.core.mail import send_mail
from .sms import send_sms

# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, "portfolio/home.html", {
        'projects':projects
    })

def resume(request):
    return render(request, "portfolio/resume.html")

def contact_success(request):
    return render(request, 'portfolio/contact_success.html')

def contact(request):
    form = ContactForm() 

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
            )
            contact.save()
            send_sms(
                message=f'{contact.name}! sent a message\n{contact.subject}, this is the message: {contact.message} You can call the person {contact.phone_number}'
            )
            return render(request, 'portfolio/contact_success.html')

    return render(request, "portfolio/contact.html", {'form': form})

