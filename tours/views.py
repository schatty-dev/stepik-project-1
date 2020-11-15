from django.shortcuts import render
from django.http import HttpResponseNotFound

MAX_TOUR_ID = 10


def main_view(request):
    return render(request, "tours/index.html")


def departure_view(request, departure):
    return render(request, "tours/departure.html", context={"departure": departure})


def tour_view(request, id):
    if id < 0 or id > MAX_TOUR_ID:
        return HttpResponseNotFound("404: Page not found :(")

    return render(request, "tours/tour.html", context={"tour_id": id})


def handler404(request, exception):
    response = render(request, '404.html', status=400)
    return response


def handler500(request):
    response = render(request, '500.html', status=500)
    return response
