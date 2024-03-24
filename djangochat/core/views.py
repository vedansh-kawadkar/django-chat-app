from django.shortcuts import render
from .forms import SignUpForm, LoginForm, CreateRoomForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from rooms.models import Room, RoomMembership, Friends
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def frontpage(request):
    if request.user.is_authenticated:
        user_name = request.session.get("username")
        user_id = User.objects.get(username=user_name).id
        rooms = RoomMembership.objects.filter(user=user_id)
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
            
            request.session['username'] = request.POST.get('username')
            
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
    if request.method == "POST":
        searchkey = request.POST.get("searchkey")
        search_results_room = Room.objects.filter(name__contains=searchkey)
        search_results_users = User.objects.filter(username__contains=searchkey)
        print(search_results_room)
        print(search_results_users)
        
        return render(request, "core/search_friends_or_grp.html", context={
            "search_users":search_results_users,
            "search_results_room":search_results_room
        })
    return render(request, "core/search_friends_or_grp.html")