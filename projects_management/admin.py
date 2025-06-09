#from django.contrib import admin
# Register your models here.
# projects_management/admin.py

from django.contrib import admin
from .models import Status, Project

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',) # Permite filtrar por status no admin

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'start_date')
    list_filter = ('status', 'start_date') # Permite filtrar por status e data
    search_fields = ('name',) # Permite pesquisar por nome do projeto
    raw_id_fields = ('status',) # Opcional: para selects grandes de Status, mostra um ID em vez de um dropdown
