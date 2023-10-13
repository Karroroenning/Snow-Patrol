from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


def index(request):
    """A view to render the index page"""

    return render(request, 'home/index.html')
