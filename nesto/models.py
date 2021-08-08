from django.db import models

# Create your models here.
class About(models.model):
    description = models.TextField()
    top_skills = models.CharField(max_length=30)

class Achievement(models.Model):
    project_count = models.CharField(max_length=15)

class Expertise(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    icon = models.ImageField()

class Banner(models.Model):
    coffee=models.IntegerField()
    projects_done = models.IntegerField()
    clients = models.IntegerField()
    patners = models.IntegerField()

class Education(models.Model):
    course = models.CharField(max_length=50)
    description = models.TextField()

class WorkExperience(models.Model):
    role = models.CharField(max_length=50)
    description = models.TextField()