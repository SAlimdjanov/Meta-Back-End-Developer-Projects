"""
views.py

"""

from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu



def home(request):
    """Home page view

    Args:
        request (HttpRequest): HTTP request object

    Returns:
        HttpResponse: Rendered view from template
    """
    return render(request, 'index.html')

def about(request):
    """About page view

    Args:
        request (HttpRequest): HTTP request object

    Returns:
        HttpResponse: Rendered view from template
    """
    return render(request, 'about.html')

def book(request):
    """Booking page view

    Args:
        request (HttpRequest): HTTP request object

    Returns:
        HttpResponse: Rendered view from template
    """
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)
