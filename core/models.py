from random import choices
from django.db import models


class Todo(models.Model):

    nome = models.CharField(max_length=36)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome