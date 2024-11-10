from django.shortcuts import render
from .decorators import admin_required

@admin_required
def admin_dashboard(request):
    # Logic for the admin view
    return render(request, 'admin_dashboard.html')
