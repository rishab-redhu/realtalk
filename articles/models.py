from django.db import models

# Create your database models here.

#1. this class inherit from model.Model. Every single model inherits from this. 
#2. model.Models verifies what we type here works with Django based database
#3. any change here --> python manage.py makemigrations

class Article(models.Model):
    title= models.TextField()
    content= models.TextField()
    