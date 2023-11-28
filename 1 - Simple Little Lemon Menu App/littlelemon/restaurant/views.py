"""
views.py

"""

# from django.http import HttpResponse
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
    return render(request, "index.html")


def about(request):
    """About page view

    Args:
        request (HttpRequest): HTTP request object

    Returns:
        HttpResponse: Rendered view from template
    """
    return render(request, "about.html")


def book(request):
    """Booking page view

    Args:
        request (HttpRequest): HTTP request object

    Returns:
        HttpResponse: Rendered view from template
    """
    form = BookingForm()

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}

    return render(request, "book.html", context)


def menu(request):
    """Booking page view

    Args:
        request (HttpRequest): HTTP request object

    Returns:
        HttpResponse: Rendered view from template
    """
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}

    return render(request, "menu.html", main_data)


def display_menu_item(request, pk=None):
    """Display a menu item view

    Args:
        request (HttpRequest): HTTP request object
        pk (int, optional): Primary key value. Defaults to None.

    Returns:
        HttpResponse: Rendered view from template
    """
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = " "

    item_dict = {"menu_item": menu_item}

    return render(request, "menu_item.html", item_dict)
