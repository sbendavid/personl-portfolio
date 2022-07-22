from http.client import HTTPResponse
from django.shortcuts import render
from .models import Project
# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, "portfolio/home.html", {
        'projects':projects
    })

def resume(request):
    return render(request, "portfolio/resume.html")

