from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message, RoomMembership
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid



# Create your views here.

@login_required
def rooms(request):
    user_name = request.session.get("username")
    user_id = User.objects.get(username=user_name).id
    print("name: ",user_name, "id: ", user_id)
    rooms = RoomMembership.objects.filter(user=user_id)
    print("rooms: ", rooms)
    
    return render(request, 'rooms/rooms.html', {
        "rooms":rooms
    })
    
@login_required
def room(request, slug):
    rooms = Room.objects.all()
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
    return render(request, 'rooms/room.html', {
        "room":room,
        "messages":messages,
        "rooms":rooms
    })
    
    
@login_required
def create_room(request):
    if request.method=="POST":
        room_name = request.POST.get("new_room_name")
        username = request.session.get('username')
        room_id = uuid.uuid4()
        room_slug = slugify(f"{room_name}-{str(room_id)}")
        new_room = Room(name=room_name, created_by=User.objects.get(username=username), slug=room_slug)
        new_room.save()
        
        new_room_membership = RoomMembership(user=User.objects.get(username=username), room=new_room)
        new_room_membership.save()
        
        return redirect("rooms")
    else:
        return redirect("rooms")

