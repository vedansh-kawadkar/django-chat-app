from django.contrib import admin
from .models import Room
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug":("name", )
        }


admin.site.register(Room, RoomAdmin)