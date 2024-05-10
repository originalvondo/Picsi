from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, LoginForm
from django.contrib import messages

# Create your views here.
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse("Gallery:home"))
    else:
        messages.error(request, "You must Log in first")
        return redirect(reverse("Accounts:login"))
    
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("Gallery:home"))  
            else:
                messages.error(request, "Invalid Credentials")
        else:
            messages.error(request, "ERROR...Something must've gone wrong")
    else:
        form = LoginForm()

    return render(request, "Accounts/login.html", { "form": form })

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("Gallery:home"))
    else:
        form = RegisterForm()

    return render(request, "Accounts/registration.html", {
        "form": form
    })