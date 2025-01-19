from .models import*

def user_details(request):
    if request.user.is_authenticated:
        return {'user': request.user}
    return {'user': None}