import email
from django.shortcuts import render
from django.http import *
from .models import User
import bcrypt
from django.http import HttpResponse
from django.shortcuts import render, redirect
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        user = User()
        user.name = request.POST.get("name")
        user.surname = request.POST.get("surname")
        user.email = request.POST.get("email")
        user.password = request.POST.get("password")
        user.confirmPassword = request.POST.get("confirmPassword")
        user.isVerified = False
        if user.password == user.confirmPassword:
            psw = user.password.encode('utf-8', 'ignore')
            hashed = bcrypt.hashpw(psw, bcrypt.gensalt())
            user.password = hashed
            user.confirmPassword = hashed
            auth_token = str(uuid.uuid4())
            user.auth_token = auth_token
            send_mail_after_registration(user.email , auth_token) 
            user.save()
            return render(request, "succesfullyRegistered.html")
        else:
            return render(request, "register.html", {"isNotValid": "Confirm password and password are not match"})
    else:
        return render(request, "register.html")

def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/user/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )

def verify(request , auth_token):
    try:
        user = User.objects.filter(auth_token = auth_token).first()
        if user:
            if user.isVerified:
                messages.success(request, 'Your account is already verified.')
                return redirect('login')
            user.isVerified = True
            user.save()
            messages.success(request, 'Your account has been verified.')
            return render(request, 'email_confirmed.html')
        else:
            return render(request, "email_confirmation_error.html")
    except Exception as e:
        print(e)
        return redirect('/')

def login(request):
    if request.method == "POST":
        try:
            user = User.objects.filter(email = request.POST.get("email")).first()
            if user.isVerified == True:
                if user.password == request.POST.get("password"):
                    render(request, "home.html", user)
                else:
                    render(request, "login.html", {"wrongPass": "Password is wrong"})
            else:
                render(request, "login.html", {"isNotVerified": "Your email is not verified"})
        except Exception as e:
            print(e)
            return redirect('login')
            #render(request, "login.html")
    else:
        return redirect('login')
        #render(request, "login.html")