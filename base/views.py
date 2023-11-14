from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def home_page(request):
    if request.user.is_authenticated:
        context = {}
        return render(request, 'base/home.html', context)
    else:
        return render(request, 'authentication/login.html')
