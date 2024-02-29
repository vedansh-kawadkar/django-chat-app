from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.rooms, name='rooms'),
    path('<slug:slug>/', view=views.room, name='room')
]
