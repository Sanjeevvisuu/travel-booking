from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from .models import *


@csrf_exempt
def about(request):
    about = about_us.objects.all()
    return render(request, "about/index.html", {'about': about})
