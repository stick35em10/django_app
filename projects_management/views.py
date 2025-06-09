#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectoForm

def lista_projectos(request):
    projectos = Project.objects.all()
    # projectos/lista.html done in 8. (Opcional) Crie templates
    return render(request, 'projects_management/lista.html', {'projectos': projectos})

def criar_projecto(request):
    if request.method == 'POST':
        form = ProjectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_projectos')
    else:
        form = ProjectoForm()
        # must do in 8. (Opcional) Crie templates
    return render(request, 'projects_management/form.html', {'form': form})

def atualizar_status(request, pk, novo_status):
    projecto = get_object_or_404(Project, pk=pk)
    projecto.status = novo_status
    projecto.save()
    return redirect('lista_projectos')
