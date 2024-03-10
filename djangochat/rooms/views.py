from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message
from django.utils.text import slugify
import uuid



# Create your views here.

@login_required
def rooms(request):
    rooms = Room.objects.all()
    
    return render(request, 'rooms/rooms.html', {
        "rooms":rooms
    })
    
@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
    return render(request, 'rooms/room.html', {
        "room":room,
        "messages":messages
    })
    
    
@login_required
def create_room(request):
    if request.method=="POST":
        room_name = request.POST.get("new_room_name")
        username = request.session.get('username')
        room_id = uuid.uuid4()
        new_room = Room(name=room_name, created_by=username, slug=slugify(room_name+str(room_id)))
        new_room.save()
        
        a = Room.objects.get(name=room_name)
        print(a.slug)
        return redirect("rooms")
    else:
        return redirect("rooms")

