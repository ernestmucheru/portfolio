from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    about = About.objects.all()
    achievements = Achievement.objects.all()
    skills = Expertise.objects.all()
    banner = Banner.objects.all()
    courses = Education.objects.all()
    work = WorkExperience.objects.all()
    projects = Projects.objects.all()

    context = {'about': about, 'achievements':achievements,'skills':skills, 'banner':banner,'courses':courses, 'work':work,'projects':projects}
    return render(request, 'home.html',context)
