from django.db import models

# Create your models here.

class Project(models.Model):
    role = models.CharField(max_length=100, default='Default Role')  # Set your desired default value
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    telephone = models.CharField(max_length=25)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.subject})"