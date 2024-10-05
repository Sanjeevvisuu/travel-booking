from django.db import models


# Create your models here.

# ooty


class ooty_package_booking_details(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    phone_no = models.CharField(max_length=10)
    pick_up = models.CharField(max_length=255)
    drop = models.CharField(max_length=255)
    package = models.CharField(max_length=100, default="ooty")
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    order_id = models.CharField(max_length=250, null=True, blank=True)
    payment_id = models.CharField(max_length=250, null=True, blank=True)
    paid = models.BooleanField(default=False)
    created_at_D_T = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

 # coonoor


class coonoor_package_booking_details(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    phone_no = models.CharField(max_length=10)
    pick_up = models.CharField(max_length=255)
    drop = models.CharField(max_length=255)
    package = models.CharField(max_length=100, default="coonoor")
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    order_id = models.CharField(max_length=250, null=True, blank=True)
    payment_id = models.CharField(max_length=250, null=True, blank=True)
    paid = models.BooleanField(default=False)
    created_at_D_T = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# masinagudi


class masinagudi_package_booking_details(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    phone_no = models.CharField(max_length=10)
    pick_up = models.CharField(max_length=255)
    drop = models.CharField(max_length=255)
    package = models.CharField(max_length=100, default="masinagudi")
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    order_id = models.CharField(max_length=250, null=True, blank=True)
    payment_id = models.CharField(max_length=250, null=True, blank=True)
    paid = models.BooleanField(default=False)
    created_at_D_T = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# manjoor


class manjoor_package_booking_details(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    phone_no = models.CharField(max_length=10)
    pick_up = models.CharField(max_length=255)
    drop = models.CharField(max_length=255)
    package = models.CharField(max_length=100, default="manjoor")
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    order_id = models.CharField(max_length=250, null=True, blank=True)
    payment_id = models.CharField(max_length=250, null=True, blank=True)
    paid = models.BooleanField(default=False)
    created_at_D_T = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# combo_pack


class comb_package_booking_details(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    phone_no = models.CharField(max_length=10)
    pick_up = models.CharField(max_length=255)
    drop = models.CharField(max_length=255)
    package = models.CharField(max_length=100, default="combo")
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    places = models.CharField(max_length=200)

    order_id = models.CharField(max_length=250, null=True, blank=True)
    payment_id = models.CharField(max_length=250, null=True, blank=True)
    paid = models.BooleanField(default=False)
    created_at_D_T = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class other_package_booking_details(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    phone_no = models.CharField(max_length=10)
    pick_up = models.CharField(max_length=255)
    drop = models.CharField(max_length=255)
    package = models.CharField(max_length=100, default="combo")
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    places = models.CharField(max_length=200)

    order_id = models.CharField(max_length=250, null=True, blank=True)
    payment_id = models.CharField(max_length=250, null=True, blank=True)
    paid = models.BooleanField(default=False)
    created_at_D_T = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
