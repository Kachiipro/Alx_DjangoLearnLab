from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

# Role-checking function for admin role
def is_admin(user):
    try:
        return user.userprofile.role == 'Admin'
    except UserProfile.DoesNotExist:
        return False

@user_passes_test(is_admin)  # Restrict access to Admin users only
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
