from django.urls import path
from . import views
from payment.views import *
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),

    path('ooty_specific/<id>/',
         views.specific_ooty_card, name='ooty_specific'),
    path("coonoor_specific/<id>/",
         views.specific_coonoor_card, name="coonoor_specific"),
    path("manjoor_specific/<id>/",
         views.specific_manjoor_card, name="manjoor_specific"),
    path("masinagudi_specific/<id>/",
         views.specific_masinagudi_card, name="masinagudi_specific"),
    path("specific_combo_pack/<id>/",
         views.specific_combo_pack, name="combo_pack"),
    path("specific_other_pack/<id>", views.specific_other_pack, name="other_pack"),


]
