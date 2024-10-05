from django.shortcuts import render, redirect

# Create your views here.

from django.conf import settings
from .models import *
from contact.models import *
from product.models import *
from booking.models import *
from website_app.models import *
from django.views.decorators.csrf import csrf_exempt
import razorpay
from tourist.settings import RAZORPAY_PRODUCT_ID, RAZORPAY_SECRET_KEY
# Create your views here.


@csrf_exempt
def payment_success(request):

    return render(request, "payment/success.html",)


@csrf_exempt
def payment_fail(request):
    return render(request, "payment/fail.html")


# checkoutsession_for_ooty_package


@csrf_exempt
def checkoutsession_for_ooty_package(request, id):
    card = ooty_packages.objects.get(id=id)
    # Normally it will be in paise; to convert into rupees, we need to multiply price * 100
    amount = int(card.price) * 100
    order_currency = 'INR'

    client = razorpay.Client(auth=(RAZORPAY_PRODUCT_ID, RAZORPAY_SECRET_KEY))

    # Assuming 'name' is part of the form data (POST request)
    name = request.POST.get('name', '')

    response_payment = client.order.create({
        "amount": amount,
        "currency": order_currency,
        'payment_capture': "1",
    })

    # We take order ID and status
    # print(response_payment)
    order_id = response_payment['id']
    order_status = response_payment['status']

    # Order creation successful
    if order_status == 'created' and order_id:
        recently_created_bok = ooty_package_booking_details.objects.order_by(
            '-id').first()
        if recently_created_bok:
            recently_created_bok.order_id = order_id
            recently_created_bok.save()

        response_payment['name'] = name
        context = {
            'card': card,
            'order_id': order_id,
            'RAZORPAY_PRODUCT_ID': RAZORPAY_PRODUCT_ID,
            'RAZORPAY_SECRET_KEY': RAZORPAY_SECRET_KEY,
            'amount': amount,
            'currency': order_currency,
            'payment': response_payment,
            'name': name,  # Pass the name to the template
        }

    return render(request, 'payment/ooty_payment_page.html', {'card': card, 'order_id': order_id, 'RAZORPAY_PRODUCT_ID': RAZORPAY_PRODUCT_ID, 'RAZORPAY_SECRET_KEY': RAZORPAY_SECRET_KEY, 'amount': amount, 'currency': order_currency, 'payment': response_payment, "context": context})


@csrf_exempt
def ooty_payment_status(request):
    contact = contact_us.objects.all()
    response = request.POST
    # print(response)to view all responses
    para_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }
    # instance
    client = razorpay.Client(auth=(RAZORPAY_PRODUCT_ID, RAZORPAY_SECRET_KEY))
    try:
        client.utility.verify_payment_signature(para_dict)  # we pass para_dict
        bok = ooty_package_booking_details.objects.get(
            # order is equal to this responce id
            order_id=response['razorpay_order_id'])
        # then save
        bok.payment_id = response['razorpay_payment_id']
        bok.paid = True
        bok.save()
        return render(request, 'payment/success.html', {"contact": contact, "bok": bok})
    except:
        return render(request, 'payment/success.html', {"contact": contact, "bok": bok, "bok": bok})
# checkoutsession_for_coonoor_package


@csrf_exempt
def checkoutsession_for_coonoor_package(request, id):
    card = coonoor_packages.objects.get(id=id)
    amount = int(card.price) * 100
    order_currency = 'INR'
    client = razorpay.Client(auth=(RAZORPAY_PRODUCT_ID, RAZORPAY_SECRET_KEY))
    name = request.POST.get('name', '')
    response_payment = client.order.create({
        "amount": amount,
        "currency": order_currency,
        'payment_capture': "1",
    })
    order_id = response_payment['id']
    order_status = response_payment['status']
    if order_status == 'created' and order_id:
        recently_created_bok = coonoor_package_booking_details.objects.order_by(
            '-id').first()
        if recently_created_bok:
            recently_created_bok.order_id = order_id
            recently_created_bok.save()
        response_payment['name'] = name
        context = {
            'card': card,
            'order_id': order_id,
            'RAZORPAY_PRODUCT_ID': RAZORPAY_PRODUCT_ID,
            'RAZORPAY_SECRET_KEY': RAZORPAY_SECRET_KEY,
            'amount': amount,
            'currency': order_currency,
            'payment': response_payment,
        }

    return render(request, 'payment/coonoor_payment_page.html', {'card': card, 'order_id': order_id, 'RAZORPAY_PRODUCT_ID': RAZORPAY_PRODUCT_ID, 'RAZORPAY_SECRET_KEY': RAZORPAY_SECRET_KEY, 'amount': amount, 'currency': order_currency, 'payment': response_payment, "context": context})


@csrf_exempt
def coonoor_payment_status(request):
    contact = contact_us.objects.all()
    response = request.POST
    # print(response)to view all responses

    para_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }
    # instance
    client = razorpay.Client(auth=(RAZORPAY_PRODUCT_ID, RAZORPAY_SECRET_KEY))
    try:
        client.utility.verify_payment_signature(para_dict)
        bok = coonoor_package_booking_details.objects.get(
            order_id=response['razorpay_order_id'])
        bok.payment_id = response['razorpay_payment_id']
        bok.paid = True
        bok.save()
        return render(request, 'payment/success.html', {"contact": contact, "bok": bok})
    except:
        return render(request, 'payment/success.html', {"contact": contact, "bok": bok})
# checkoutsession_for_masinagudi_package


@csrf_exempt
def checkoutsession_for_masinagudi_package(request, id):
    card = masinagudi_packages.objects.get(id=id)
    amount = int(card.price) * 100
    order_currency = 'INR'
    client = razorpay.Client(auth=(RAZORPAY_PRODUCT_ID, RAZORPAY_SECRET_KEY))
    name = request.POST.get('name', '')
    response_payment = client.order.create({
        "amount": amount,
        "currency": order_currency,
        'payment_capture': "1",
    })
    order_id = response_payment['id']
    order_status = response_payment['status']
    if order_status == 'created' and order_id:
        recently_created_bok = masinagudi_package_booking_details.objects.order_by(
            '-id').first()  # to call recently alterd colum
        if recently_created_bok:
            recently_created_bok.order_id = order_id
            recently_created_bok.save()
        response_payment['name'] = name
        context = {
            'card': card,
            'order_id': order_id,
            'RAZORPAY_PRODUCT_ID': RAZORPAY_PRODUCT_ID,
            'RAZORPAY_SECRET_KEY': RAZORPAY_SECRET_KEY,
            'amount': amount,
            'currency': order_currency,
            'payment': response_payment,
        }

    return render(request, 'payment/masinagudi_payment_page.html', {'card': card, 'order_id': order_id, 'RAZORPAY_PRODUCT_ID': RAZORPAY_PRODUCT_ID, 'RAZORPAY_SECRET_KEY': RAZORPAY_SECRET_KEY, 'amount': amount, 'currency': order_currency, 'payment': response_payment, "context": context})


@csrf_exempt
def masinagudi_payment_status(request):
    contact = contact_us.objects.all()
    response = request.POST
    # print(response)to view all responses

    para_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }
    # instance
    client = razorpay.Client(auth=(RAZORPAY_PRODUCT_ID, RAZORPAY_SECRET_KEY))
    try:
        client.utility.verify_payment_signature(para_dict)
        bok = masinagudi_package_booking_details.objects.get(
            order_id=response['razorpay_order_id'])
        bok.payment_id = response['razorpay_payment_id']
        bok.paid = True
        bok.save()
        return render(request, 'payment/success.html', {"contact": contact, "bok": bok})
    except:
        return render(request, 'payment/success.html', {"contact": contact, "bok": bok})


# checkoutsession_for_manjoor_package


@csrf_exempt
def checkoutsession_for_manjoor_package(request, id):
    card = manjoor_packages.objects.get(id=id)
    amount = int(card.price) * 100
    order_currency = 'INR'
    client = razorpay.Client(auth=(RAZORPAY_PRODUCT_ID, RAZORPAY_SECRET_KEY))
    name = request.POST.get('name', '')
    response_payment = client.order.create({
        "amount": amount,
        "currency": order_currency,
        'payment_capture': "1",
    })
    order_id = response_payment['id']
    order_status = response_payment['status']
    if order_status == 'created' and order_id:
        recently_created_bok = manjoor_package_booking_details.objects.order_by(
            '-id').first()
        if recently_created_bok:
            recently_created_bok.order_id = order_id
            recently_created_bok.save()
        response_payment['name'] = name
        context = {
            'card': card,
            'order_id': order_id,
            'RAZORPAY_PRODUCT_ID': RAZORPAY_PRODUCT_ID,
            'RAZORPAY_SECRET_KEY': RAZORPAY_SECRET_KEY,
            'amount': amount,
            'currency': order_currency,
            'payment': response_payment,
        }

    return render(request, 'payment/manjoor_payment_page.html', {'card': card, 'order_id': order_id, 'RAZORPAY_PRODUCT_ID': RAZORPAY_PRODUCT_ID, 'RAZORPAY_SECRET_KEY': RAZORPAY_SECRET_KEY, 'amount': amount, 'currency': order_currency, 'payment': response_payment, "context": context})


@csrf_exempt
def manjoor_payment_status(request):
    contact = contact_us.objects.all()
    response = request.POST
    # print(response)to view all responses

    para_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }
    # instance
    client = razorpay.Client(auth=(RAZORPAY_PRODUCT_ID, RAZORPAY_SECRET_KEY))
    try:
        client.utility.verify_payment_signature(para_dict)
        bok = manjoor_package_booking_details.objects.get(
            order_id=response['razorpay_order_id'])
        bok.payment_id = response['razorpay_payment_id']
        bok.paid = True
        bok.save()
        return render(request, 'payment/success.html', {"contact": contact, "bok": bok})
    except:
        return render(request, 'payment/success.html', {"contact": contact, "bok": bok})


# combo pack


@csrf_exempt
def checkoutsession_for_combo_package(request, id):
    card = owl_combo_packages.objects.get(id=id)
    amount = int(card.price) * 100
    order_currency = 'INR'
    client = razorpay.Client(auth=(RAZORPAY_PRODUCT_ID, RAZORPAY_SECRET_KEY))
    name = request.POST.get('name', '')
    response_payment = client.order.create({
        "amount": amount,
        "currency": order_currency,
        'payment_capture': "1",
    })
    order_id = response_payment['id']
    order_status = response_payment['status']
    if order_status == 'created' and order_id:
        recently_created_bok = comb_package_booking_details.objects.order_by(
            '-id').first()
        if recently_created_bok:
            recently_created_bok.order_id = order_id
            recently_created_bok.save()
        response_payment['name'] = name
        context = {
            'card': card,
            'order_id': order_id,
            'RAZORPAY_PRODUCT_ID': RAZORPAY_PRODUCT_ID,
            'RAZORPAY_SECRET_KEY': RAZORPAY_SECRET_KEY,
            'amount': amount,
            'currency': order_currency,
            'payment': response_payment,
        }

    return render(request, 'payment/combo_pack_payment_page.html', {'card': card, 'order_id': order_id, 'RAZORPAY_PRODUCT_ID': RAZORPAY_PRODUCT_ID, 'RAZORPAY_SECRET_KEY': RAZORPAY_SECRET_KEY, 'amount': amount, 'currency': order_currency, 'payment': response_payment, "context": context})


@csrf_exempt
def combo_package_payment_status(request):
    contact = contact_us.objects.all()
    response = request.POST
    # print(response)to view all responses

    para_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }
    # instance
    client = razorpay.Client(auth=(RAZORPAY_PRODUCT_ID, RAZORPAY_SECRET_KEY))
    try:
        client.utility.verify_payment_signature(para_dict)
        bok = comb_package_booking_details.objects.get(
            order_id=response['razorpay_order_id'])
        bok.payment_id = response['razorpay_payment_id']
        bok.paid = True
        bok.save()
        return render(request, 'payment/success.html', {"contact": contact, "bok": bok})
    except:
        return render(request, 'payment/success.html', {"contact": contact, "bok": bok})


# other_packages


@csrf_exempt
def checkoutsession_for_other_package(request, id):
    card = packages.objects.get(id=id)
    amount = int(card.price) * 100
    order_currency = 'INR'
    client = razorpay.Client(auth=(RAZORPAY_PRODUCT_ID, RAZORPAY_SECRET_KEY))
    name = request.POST.get('name', '')
    response_payment = client.order.create({
        "amount": amount,
        "currency": order_currency,
        'payment_capture': "1",
    })
    order_id = response_payment['id']
    order_status = response_payment['status']
    if order_status == 'created' and order_id:
        recently_created_bok = other_package_booking_details.objects.order_by(
            '-id').first()
        if recently_created_bok:
            recently_created_bok.order_id = order_id
            recently_created_bok.save()
        response_payment['name'] = name
        context = {
            'card': card,
            'order_id': order_id,
            'RAZORPAY_PRODUCT_ID': RAZORPAY_PRODUCT_ID,
            'RAZORPAY_SECRET_KEY': RAZORPAY_SECRET_KEY,
            'amount': amount,
            'currency': order_currency,
            'payment': response_payment,
        }

    return render(request, 'payment/other_pack_payment_page.html', {'card': card, 'order_id': order_id, 'RAZORPAY_PRODUCT_ID': RAZORPAY_PRODUCT_ID, 'RAZORPAY_SECRET_KEY': RAZORPAY_SECRET_KEY, 'amount': amount, 'currency': order_currency, 'payment': response_payment, "context": context})


@csrf_exempt
def other_pack_payment_status(request):
    contact = contact_us.objects.all()
    response = request.POST
    # print(response)to view all responses

    para_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }
    # instance
    client = razorpay.Client(auth=(RAZORPAY_PRODUCT_ID, RAZORPAY_SECRET_KEY))
    try:
        client.utility.verify_payment_signature(para_dict)
        bok = other_package_booking_details.objects.get(
            order_id=response['razorpay_order_id'])
        bok.payment_id = response['razorpay_payment_id']
        bok.paid = True
        bok.save()
        return render(request, 'payment/success.html', {"contact": contact, "bok": bok})
    except:
        return render(request, 'payment/success.html', {"contact": contact, "bok": bok})
