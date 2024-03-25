from django.shortcuts import render
from .forms import SignUpForm, LoginForm, CreateRoomForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from rooms.models import Room, RoomMembership, Friends, UserChat
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
import uuid
from django.utils.text import slugify

# Create your views here.


def frontpage(request):
    if request.user.is_authenticated:
        user_name = request.session.get("username")
        user_id = User.objects.get(username=user_name).id
        request.session["user_id"] = user_id
        rooms = RoomMembership.objects.filter(user=user_id)
        cache.set("rooms", rooms)
        return render(request, "core/frontpage.html", context={
            "rooms":rooms
        })
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = request.POST.get('username')
            request.session['username'] = username
            user_chat_id = uuid.uuid4()
            user_chat = UserChat(name=username, room_id=user_chat_id, slug=slugify(username+str(user_chat_id)))
            user_chat.save()
            
            return redirect('frontpage')
    else:
        form = SignUpForm()
        
    return render(request, 'core/signup.html', {
        "form":form
    })
    
    
def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        has_errors = True
        if user:
            has_errors = False
            request.session.set_expiry(1200)
            login(request, user)
            request.session['username'] = request.POST.get('username')
                        
            return redirect('frontpage')
            
        errors = "Invalid Credentials"
        return render(request, 'core/login.html', {
            "errors":errors, 
            "has_errors":has_errors
        })
        
    else:
        return render(request, 'core/login.html')
    
@login_required
def search(request):
    user_id = request.session.get("user_id")
    print(user_id)
    rooms = RoomMembership.objects.filter(user=user_id)
    if request.method == "POST":
        searchkey = request.POST.get("searchkey")
        print("search key: ", searchkey)
        search_results_room = Room.objects.filter(name__icontains=searchkey)
        search_results_users = User.objects.filter(username__icontains=searchkey)
        print(search_results_room)
        print(search_results_users)
        
        return render(request, "core/search_friends_or_grp.html", context={
            "search_result_users":search_results_users,
            "search_result_groups":search_results_room,
            "rooms":rooms
        })
    return render(request, "core/search_friends_or_grp.html", {
        "rooms":rooms
    })