from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=25)
    owner=models.ForeignKey("auth.user",  on_delete=models.CASCADE)