from django.urls import path

from . import views

urlpatterns = [
    path('room/<slug:slug>/', view=views.room, name='room'),
    path('new_room/', view=views.create_room, name='new_room'),
    path('room/<slug:slug>/join/', view=views.join_chat_room, name="join_chat_room"),
    path('room/<slug:slug>/add_participant/', view=views.add_participant_to_room, name="add_participant")
]
