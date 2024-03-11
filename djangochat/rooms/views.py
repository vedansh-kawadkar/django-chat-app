from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message, RoomMembership
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid



# Create your views here.

@login_required
def rooms(request):
    print("rooms view called")
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
    print(f"room: {slug} accessed")
    user_name = request.session.get("username")
    user_id = User.objects.get(username=user_name).id
    print("name: ",user_name, "id: ", user_id)
    rooms = RoomMembership.objects.filter(user=user_id)
    
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
        print("new room create view called")
        room_name = request.POST.get("room_name")
        description = request.POST.get("description")
        is_public = True if request.POST.get("is_public")=="on" else False
        
        username = request.session.get('username')
        room_id = uuid.uuid4()
        room_slug = slugify(f"{room_name}-{str(room_id)}")
        new_room = Room(name=room_name, created_by=User.objects.get(username=username), slug=room_slug, description=description, is_public=is_public)
        new_room.save()
        
        new_room_membership = RoomMembership(user=User.objects.get(username=username), room=new_room)
        new_room_membership.save()
        
        return redirect("rooms")
    else:
        return redirect("rooms")

