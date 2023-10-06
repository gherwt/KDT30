from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    major = models.CharField(max_length=10)
    description = models.TextField()