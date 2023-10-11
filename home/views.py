from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import SubscribedUsers

from django.contrib import messages


def index(request):
    """A view to render the index page"""

    return render(request, 'home/index.html')


def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(request, "You must type legit name and email to subscribe to a Newsletter")
            return redirect("home")

        if get_user_model().objects.filter(email=email).first():
            messages.error(request, f"Found registered user with associated {email} email. You must login to subscribe or unsubscribe.")
            return redirect(request.META.get("HTTP_REFERER", "home")) 

        subscribe_user = SubscribedUsers.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "home"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("home")

        subscribe_model_instance = SubscribedUsers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "home"))
