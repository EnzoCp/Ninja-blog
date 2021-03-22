from django.db import models


class Post(models.Model):
    title = models.CharField('Titulo', max_length=64)
    content = models.TextField('Conteudo')
