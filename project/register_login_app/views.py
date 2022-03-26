from django.shortcuts import render
from django.http import *
from .models import User

def index(request):
    return render(request, "register.html")

def register(request):
    if request.method == "POST":
        user = User()
        user.name = request.POST.get("name")
        user.surname = request.POST.get("surname")
        user.email = request.POST.get("email")
        user.password = request.POST.get("password")
        user.confirmPassword = request.POST.get("confirmPassword")
        if user.password == user.confirmPassword:
            user.save()
            return render(request, "succesfullyRegistered.html")
        else:
            return render(request, "register.html", {"isValid": False})
    else:
        return HttpResponseRedirect("/")


