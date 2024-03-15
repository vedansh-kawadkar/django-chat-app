from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid

# Create your models here.

class RoomManager(models.Manager):
    def users_allowed(self, room):
        return self.get(name=room).memberships.filter(is_allowed=True).select_related('user')

    
class Room(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, db_index=True, default="", null=False) 
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    room_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, null=False)
    is_public = models.BooleanField(default=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    
    objects = RoomManager()
    
    def __str__(self) -> str:
        return f"{self.name} created by {self.created_by}"


class RoomMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    is_allowed = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('user', 'room',)
        
    def __str__(self):
        return f"{self.user} present in {self.room}"
    

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    message_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('date_added', )


class Friends(models.Model):
    friend1 = models.ForeignKey(User, related_name="friend1_of_friend2", on_delete=models.CASCADE)
    friend2 = models.ForeignKey(User, related_name="friend2_of_friend1", on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('friend1', 'friend2',)