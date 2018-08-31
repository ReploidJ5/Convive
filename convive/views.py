from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.urls import reverse


@login_required
def index(request):
    if (request.user.is_staff!=True and request.user.email[-12:]!="miumg.edu.gt"):
        request.user.delete()
        return render(request, "login.html")
    return render(request, 'index.html')

def Login(request):
    if request.method == "GET":
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))

