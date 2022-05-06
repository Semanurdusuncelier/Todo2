from turtle import title
from django.db import models

# Create your models here.
class Todo(models.Model):
      title=models.CharField(max_length=200,verbose_name="Title")
      completed=models.BooleanField(verbose_name="Status")

def __str__(self):
    return self.title
