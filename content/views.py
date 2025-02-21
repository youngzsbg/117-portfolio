from django.shortcuts import render
from.models import Project

# Create your views here.

def project_list_view(request):
    my_projects = Project.objects.all()
    
    return render(request, "pages/project_list.html", {"projects":my_projects})
