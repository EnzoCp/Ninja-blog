from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('Titulo', max_length=64)
    content = models.TextField('Conteudo')

    def __str__(self):
        return f'{self.owner} - {self.title}'