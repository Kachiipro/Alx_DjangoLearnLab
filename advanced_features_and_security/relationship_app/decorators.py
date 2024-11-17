from django.http import HttpResponseForbidden
from functools import wraps
from .models import UserProfile

def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("You are not authorized to access this page.")
            
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                if user_profile.role == role:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponseForbidden("You do not have the necessary permissions to view this page.")
            except UserProfile.DoesNotExist:
                return HttpResponseForbidden("You do not have the necessary permissions to view this page.")
        
        return _wrapped_view
    return decorator

admin_required = role_required("Admin")
librarian_required = role_required("Librarian")
member_required = role_required("Member")
