from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=100, unique=True)
    definition = models.TextField()
    synonymns = models.CharField(max_length=255)
    def __str__(self):
        return self.word
