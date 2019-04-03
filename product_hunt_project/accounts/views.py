from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib import auth
from django.shortcuts import redirect


# Create your views here.
# create user
def signup(request):
    if request.method == "POST":
        # check email already exist
        try:
            user = User.objects.get(email=request.POST['email'])
            return render(request, "accounts/signup.html", {'error':'this email in use try another'})
        except User.DoesNotExist:
            user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'] )
            auth.login(request, user)
            return redirect('home')
    else:
        return render(request, "accounts/signup.html")


# login
def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return  redirect('home')
        else:
            return render(request, "accounts/login.html",{'error':"email or password  does not matched"})


    else:
        return render(request, "accounts/login.html")


# logout
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("home")