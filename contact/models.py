from django.db import models

# Create your models here.


class contact_us(models.Model):
    name = models.CharField(max_length=150)
    travel_name = models.CharField(max_length=200)
    ph_no = models.IntegerField()
    address = models.CharField(max_length=250)
    wathsapp_no = models.IntegerField()

    def __str__(self):
        return self.name
