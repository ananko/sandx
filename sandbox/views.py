from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def overview(request):
    return render(request, 'sandbox/overview.html', {})

@login_required
def profile(request):
    return render(request, 'sandbox/profile.html', {})

