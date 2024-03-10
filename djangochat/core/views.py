from django.shortcuts import render
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
# Create your views here.


def frontpage(request):
    return render(request, "core/frontpage.html")

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
            return redirect('frontpage')
        errors = "Invalid Credentials"
        return render(request, 'core/login.html', {
            "errors":errors, 
            "has_errors":has_errors
        })
        
    else:
        return render(request, 'core/login.html')