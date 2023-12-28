"""
views.py

"""

import json
from datetime import datetime

from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .forms import BookingForm
from .models import Menu
from .models import Booking


def home(request):
    """Homepage view"""
    return render(request, "index.html")


def about(request):
    """About page view"""
    return render(request, "about.html")


def reservations(request):
    """Reservations view"""
    # date = request.GET.get("date", datetime.today().date())
    current_bookings = Booking.objects.all()
    booking_json = serializers.serialize("json", current_bookings)
    return render(request, "bookings.html", {"bookings": booking_json})


def book(request):
    """Book view"""
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "book.html", context)


def menu(request):
    """Menu view"""
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, "menu.html", {"menu": main_data})


def display_menu_item(request, pk=None):
    """Display a menu item"""
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, "menu_item.html", {"menu_item": menu_item})


@csrf_exempt
def bookings(request):
    """Bookings"""
    if request.method == "POST":
        data = json.load(request)
        exist = (
            Booking.objects.filter(reservation_date=data["reservation_date"])
            .filter(reservation_slot=data["reservation_slot"])
            .exists()
        )
        if exist is False:
            booking = Booking(
                first_name=data["first_name"],
                reservation_date=data["reservation_date"],
                reservation_slot=data["reservation_slot"],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type="application/json")

    date = request.GET.get("date", datetime.today().date())

    current_bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize("json", current_bookings)

    return HttpResponse(booking_json, content_type="application/json")
