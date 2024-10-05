from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment_success/', payment_success, name="payment_success"),
    path('payment_fail/', payment_fail, name="payment_fail"),
    path('ooty_payment_status/', ooty_payment_status, name='ooty_payment_status'),
    path('coonoor_payment_status/', coonoor_payment_status,
         name='coonoor_payment_status'),
    path('manjoor_payment_status/', manjoor_payment_status,
         name='manjoor_payment_status'),
    path('masinagudi_payment_status/', masinagudi_payment_status,
         name='masinagudi_payment_status'),
    path('combo_package_payment_status/', combo_package_payment_status,
         name='combo_package_payment_status'),
    path('other_pack_payment_status/', other_pack_payment_status,
         name='other_pack_payment_status'),

    path("checkoutsession_ooty/<id>/",
         checkoutsession_for_ooty_package, name="checkoutsession_ooty"),
    path("checkoutsession_coonoor/<id>/",
         checkoutsession_for_coonoor_package, name="checkoutsession_coonoor"),
    path("checkoutsession_masinagudi/<id>/",
         checkoutsession_for_masinagudi_package, name="checkoutsession_masinagudi"),
    path("checkoutsession_manjoor/<id>/",
         checkoutsession_for_manjoor_package, name="checkoutsession_manjoor"),
    path("checkoutsession_combo/<id>",
         checkoutsession_for_combo_package, name="checkoutsession_combo"),
    path("checkoutsession_other_pack/<id>",
         checkoutsession_for_other_package, name="checkoutsession_other_pack"),


]
