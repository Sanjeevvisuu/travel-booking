from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from booking.models import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):

    img1 = welcome_page_image_first.objects.all()
    img2 = welcome_page_image_second.objects.all()
    img3 = welcome_page_image_third.objects.all()

    com_pack = owl_combo_packages.objects.all()

    pack = packages.objects.all()

    return render(request, "welcome/index.html", {"img1": img1, "img2": img2, "img3": img3, "com_pack": com_pack, "pack": pack})


@csrf_exempt
def booking(request):
    return render(request, "booking/index.html")


@csrf_exempt
def ooty_page(request):
    cards = ooty_packages.objects.all()
    return render(request, "ooty/index.html", {"cards": cards})


@csrf_exempt
def coonoor_page(request):
    cards = coonoor_packages.objects.all()

    return render(request, "coonoor/index.html", {"cards": cards})


@csrf_exempt
def masinagudi_page(request):
    cards = masinagudi_packages.objects.all()

    return render(request, "masinagudi/index.html", {"cards": cards})


@csrf_exempt
def manjoor_page(request):
    cards = manjoor_packages.objects.all()

    return render(request, "avalanchi/index.html", {"cards": cards})
