from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, db_index=True, default="", null=False) 
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    room_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, null=False)
    
    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    message_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('date_added', )
        