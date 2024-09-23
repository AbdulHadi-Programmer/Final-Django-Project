from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_page(request):
    result = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')   # After login, redirect to home page
        else:
            result = "Username or Password is Invalid"

    return render(request, 'login.html', {'result': result})  # Render login.html


def signup_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        user_data = User.objects.create_user(username, email, password)
        user_data.save()
        return redirect("login")  # Redirect to login after signup

    return render(request, "signup.html")  # Render signup.html


def logoutpage(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def home(request):
    return render(request, 'main.html')  # Render main.html for home page
