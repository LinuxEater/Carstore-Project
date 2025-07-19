from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    facebook_link = models.URLField(max_length=200, blank=True, null=True)
    twiter_link = models.URLField(max_length=200, blank=True, null=True)
    google_link = models.URLField(max_length=200, blank=True, null=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name