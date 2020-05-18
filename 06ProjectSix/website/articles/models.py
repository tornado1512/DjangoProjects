from django.db import models

# Create your models here.
from django.urls import reverse


class Article(models.Model):
    author=models.ForeignKey(
        'auth.user',
        on_delete=models.CASCADE
    )
    title=models.CharField(max_length=300)
    text=models.TextField()
    def get_absolute_url(self):
        return reverse('home')
    def __str__(self):
        return self.title