from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Login successful, welcome {user.username}")
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "accounts/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, "accounts/register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, "accounts/register.html")

        user = User(username=username)
        user.set_password(password1)
        user.save()

        messages.success(request, "Account created successfully. You can now login.")
        return redirect("login")

    return render(request, "accounts/register.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect("/")
