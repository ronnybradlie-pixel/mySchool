from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    subject = models.CharField(max_length=80)
    email = models.EmailField()
    image=CloudinaryField('image', null=True)

    def __str__(self):
        return self.name

class School(models.Model):
    school_name = models.CharField(max_length=80)
    address = models.TextField()
    location = models.CharField(max_length=80)
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.school_name
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.email
    
    
