from django.shortcuts import render
#from django.http import HttpResponse

from .models import Project

def homepage(request):
    projects = Project.objects.all()

    return render(request, 'portfolio/homepage.html', {'projects':projects})
