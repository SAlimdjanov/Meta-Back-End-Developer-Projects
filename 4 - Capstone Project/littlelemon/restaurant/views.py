"""
views.py

"""


from django.shortcuts import render


def home(request):
    """Renders home page template

    Args:
        (django.http.HttpRequest): Request object

    Returns:
        django.http.HttpResponse: HTTP response object with loaded template
    """
    return render(request, "index.html", {})
