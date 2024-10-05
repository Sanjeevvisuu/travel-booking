from django.http import HttpResponse
from django.shortcuts import render, redirect
from website_app.models import *
from booking.models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# ooty


@csrf_exempt
def specific_ooty_card(request, id):
    card = ooty_packages.objects.get(id=id)
    if request.method == "POST":
        name = request.POST["name"]
        mail = request.POST["mail"]
        phone_no = int(request.POST["phone_no"])
        pick_up = request.POST["pick_up"]
        drop = request.POST["drop"]

        title = card.title
        price = card.price

        booking_instance = ooty_package_booking_details(
            name=name, mail=mail, phone_no=phone_no, pick_up=pick_up, drop=drop, package="ooty", title=title, price=price)

        booking_instance.save()

        return redirect("checkoutsession_ooty", id=id)
    return render(request, "Ooty/o_sp.html", {"card": card})

# coonoor


@csrf_exempt
def specific_coonoor_card(request, id):
    card = coonoor_packages.objects.get(id=id)
    if request.method == "POST":
        name = request.POST["name"]
        mail = request.POST["mail"]
        phone_no = int(request.POST["phone_no"])
        pick_up = request.POST["pick_up"]
        drop = request.POST["drop"]

        title = card.title
        price = card.price

        booking_instance = coonoor_package_booking_details(
            name=name, mail=mail, phone_no=phone_no, pick_up=pick_up, drop=drop, package="coonoor", title=title, price=price)

        booking_instance.save()

        return redirect("checkoutsession_coonoor", id=id)
    return render(request, "coonoor/c_sp.html", {"card": card})
# masinagudi


@csrf_exempt
def specific_masinagudi_card(request, id):
    card = masinagudi_packages.objects.get(id=id)
    if request.method == "POST":
        name = request.POST["name"]
        mail = request.POST["mail"]
        phone_no = int(request.POST["phone_no"])
        pick_up = request.POST["pick_up"]
        drop = request.POST["drop"]

        title = card.title
        price = card.price

        booking_instance = masinagudi_package_booking_details(
            name=name, mail=mail, phone_no=phone_no, pick_up=pick_up, drop=drop, package="masinagudi", title=title, price=price)

        booking_instance.save()

        return redirect("checkoutsession_masinagudi", id=id)
    return render(request, "masinagudi/ms_sp.html", {"card": card})
# manjoor


@csrf_exempt
def specific_manjoor_card(request, id):
    card = manjoor_packages.objects.get(id=id)
    if request.method == "POST":
        name = request.POST["name"]
        mail = request.POST["mail"]
        phone_no = int(request.POST["phone_no"])
        pick_up = request.POST["pick_up"]
        drop = request.POST["drop"]

        title = card.title
        price = card.price

        booking_instance = manjoor_package_booking_details(
            name=name, mail=mail, phone_no=phone_no, pick_up=pick_up, drop=drop, package="manjoor", title=title, price=price)

        booking_instance.save()

        return redirect("checkoutsession_manjoor", id=id)
    return render(request, "avalanchi/man_sp.html", {"card": card})
# combo pack


@csrf_exempt
def specific_combo_pack(request, id):
    card = owl_combo_packages.objects.get(id=id)
    if request.method == "POST":
        name = request.POST["name"]
        mail = request.POST["mail"]
        phone_no = int(request.POST["phone_no"])
        pick_up = request.POST["pick_up"]
        drop = request.POST["drop"]

        title = card.title
        price = card.price
        places = card.places
        booking_instance = comb_package_booking_details(
            name=name, mail=mail, phone_no=phone_no, pick_up=pick_up, drop=drop, package="combo_pack", title=title, price=price, places=places)

        booking_instance.save()

        return redirect("checkoutsession_combo", id=id)

    return render(request, "welcome_specific_owl/index.html", {"card": card})
# other packages


@csrf_exempt
def specific_other_pack(request, id):
    card = packages.objects.get(id=id)
    if request.method == "POST":
        name = request.POST["name"]
        mail = request.POST["mail"]
        phone_no = int(request.POST["phone_no"])
        pick_up = request.POST["pick_up"]
        drop = request.POST["drop"]

        title = card.title
        price = card.price
        booking_instance = other_package_booking_details(
            name=name, mail=mail, phone_no=phone_no, pick_up=pick_up, drop=drop, package="other_pack", title=title, price=price)

        booking_instance.save()

        return redirect("checkoutsession_other_pack", id=id)

    return render(request, "other_packages/index.html", {"card": card})
