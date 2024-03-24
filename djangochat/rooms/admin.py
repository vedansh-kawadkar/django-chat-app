from django.contrib import admin
from .models import Room, RoomMembership, Message
# Register your models here.



admin.site.register(Room)
admin.site.register(RoomMembership)
admin.site.register(Message)