from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Note(models.Model):
    title=CharField(max_length=100)
    desc=CharField(max_length=800)
    date=models.DateField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title