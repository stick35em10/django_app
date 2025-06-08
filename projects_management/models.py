# projects_management/models.py

from django.db import models

# Create your models here.


# from django.db import models

class Status(models.Model):
    """
    Representa o status de um projeto (e.g., To Do, Doing, Done).
    """
    # Choices para garantir que os valores sejam consistentes
    TODO = 'TODO'
    DOING = 'DOING'
    DONE = 'DONE'
    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (DOING, 'Doing'),
        (DONE, 'Done'),
    ]

    name = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        unique=True, # Garante que não haja statuses duplicados como 'To Do' e 'To Do'
        default=TODO, # Status padrão ao criar um projeto
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Uma descrição breve do status."
    )

    class Meta:
        verbose_name = "Status do Projeto"
        verbose_name_plural = "Status dos Projetos"
        ordering = ['id'] # Ordena por ID, pode ser alterado se preferir outra ordem

    def __str__(self):
        return self.get_name_display() # Retorna o valor "legível" do choice


class Project(models.Model):
    """
    Representa um projeto com um nome, data de criação e um status.
    """
    name = models.CharField(
        max_length=255,
        unique=True, # Garante que os nomes dos projetos sejam únicos
        verbose_name="Nome do Projeto"
    )
    # ForeignKey para o model Status.
    # on_delete=models.PROTECT significa que você não pode deletar um status
    # se houver projetos associados a ele. Altere para models.CASCADE se quiser
    # que os projetos sejam deletados junto com o status (geralmente não recomendado para status).
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='projects', # Define o nome para a relação inversa (e.g., status.projects.all())
        verbose_name="Status"
    )
    start_date = models.DateField(
        auto_now_add=True, # A data é automaticamente definida na criação
        verbose_name="Data de Início"
    )
    # Se quiser uma data de atualização:
    # updated_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['-start_date', 'name'] # Ordena do mais recente para o mais antigo, depois por nome

    def __str__(self):
        return self.name
