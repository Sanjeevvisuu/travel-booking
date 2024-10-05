from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.


@csrf_exempt
def index(request):
    contact = contact_us.objects.all()

    return render(request, "contact/index.html", {'contact': contact})
