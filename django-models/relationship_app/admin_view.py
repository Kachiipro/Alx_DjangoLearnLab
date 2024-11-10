from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .models import UserProfile

def admin_dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.is_admin():
        return render(request, 'admin_dashboard.html')
    return HttpResponseForbidden("You are not authorized to view this page.")