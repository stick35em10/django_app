from django.db import models

# Create your models here.

#from django.db import models

class Cam(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('DOING', 'Doing'),
        ('DONE', 'Done'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='TODO')

    def __str__(self):
        return self.get_status_display()  # Retorna a representação legível do status

class Projectos(models.Model):
    nome_do_projecto = models.CharField(max_length=255)
    status = models.ForeignKey(Cam, on_delete=models.CASCADE)  # Relacionamento com Cam
    data = models.DateField()

    def __str__(self):
        return self.nome_do_projecto
