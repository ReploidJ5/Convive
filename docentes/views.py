from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
@login_required
def docentes(request):
    request.user.is_staff=True
    request.user.save()
    return redirect(reverse('index'))
