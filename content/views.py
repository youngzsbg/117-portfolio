from django.shortcuts import render
from.models import Project
from django.views.generic import ListView
from .forms import ProjectForm


# Create your views here.

#def project_list_view(request):
    #my_projects = Project.objects.all()
    
    #return render(request, "pages/project_list.html", {"projects":my_projects})

class ProjectsListView(ListView):
    model = Project
    template_name = "pages/project_list.html"
    context_object_name = "projects"
    

def project_new_view(request):
    form = ProjectForm()
    return render(request, 'pages/project_new.html', {'form': form})