from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nome")

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    content = models.TextField(verbose_name="Conteúdo")
    created_at = models.DateTimeField(
        auto_now_add=True, auto_now=False, verbose_name="Criado em"
    )
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self) -> str:
        return self.title
