from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("ooty/", ooty_page, name="ooty"),
    path("coonoor/", coonoor_page, name="coonoor"),
    path("masinagudi/", masinagudi_page, name="masinagudi"),
    path("manjoor/", manjoor_page, name="manjoor"),

]
