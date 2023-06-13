from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phonenumber = models.IntegerField()
    message = models.TextField(max_length=200)
    
    def __str__(self):
        return self.name
    

class UserForm(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)
    
    def __str__(self):
        return self.username
    
    def Create(self):
        user = User.objects.create_user(username=self.username, email=self.email, password=self.password)
        user.save()
        return self.userid