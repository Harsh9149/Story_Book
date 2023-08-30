from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request,'main.html')

def signuppage(request):
    return render(request,'signup.html')

def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        country = request.POST['country']

        myuser = User.objects.create_user(username, email, pass1)
        # myuser.country = country
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")

    return HttpResponse("login")

def handleLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        # loginemail = request.POST['loginemail']

        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully loged in")
            return redirect('/')
        else:
            messages.error(request, "Invalid, Try Again")
            return redirect("/")

    return HttpResponse("handlelogin")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')