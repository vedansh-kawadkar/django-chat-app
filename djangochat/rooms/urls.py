from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.rooms, name='rooms'),
    path('room/<slug:slug>/', view=views.room, name='room'),
    path('new_room/', view=views.create_room, name='new_room')
]
