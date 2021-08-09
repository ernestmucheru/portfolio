from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class About(models.Model):
    description = models.TextField()

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

    def __str__(self):
        return "About Me"

class Achievement(models.Model):
    project_count = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"

    def __str__(self):
        return "Achievements"

class Expertise(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    icon = models.ImageField()

    class Meta:
        verbose_name = "Expertise"
        verbose_name_plural = "Expertise"

    def __str__(self):
        return self.title

class Banner(models.Model):
    coffee=models.IntegerField()
    projects_done = models.IntegerField()
    clients = models.IntegerField()
    patners = models.IntegerField()

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banner"

    def __str__(self):
        return "Banner"

class Education(models.Model):
    course = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"

    def __str__(self):
        return "Education"

class WorkExperience(models.Model):
    role = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experience"

    def __str__(self):
        return "role"

class Projects(models.Model): 
    image = models.ImageField()
    title = models.CharField(max_length=30)
    livelink = models.URLField(max_length=120)
    alt = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return "title"
