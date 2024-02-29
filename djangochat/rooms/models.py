from django.db import models
from django.utils.text import slugify

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True) 
    
    def __str__(self) -> str:
        return self.name
