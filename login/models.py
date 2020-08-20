from django.db import models

# Create your models here.
class Blog(models.Model):
    text= models.TextField()

class Pictures(models.Model):
    text = models.Textfield()
    image = models.ImageField(upload_to="blogimg")