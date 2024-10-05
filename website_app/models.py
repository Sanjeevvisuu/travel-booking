from django.db import models

# Create your models here.


class welcome_page_image_first(models.Model):
    image = models.ImageField(upload_to="upload_photos", null=False)
    name = models.CharField(max_length=100, default="first")

    def __str__(self) -> str:
        return self.name


class welcome_page_image_second(models.Model):
    image = models.ImageField(upload_to="upload_photos", null=False)
    name = models.CharField(max_length=100, default="secont")

    def __str__(self) -> str:
        return self.name


class welcome_page_image_third(models.Model):
    image = models.ImageField(upload_to="upload_photos", null=False)
    name = models.CharField(max_length=100, default="third")

    def __str__(self) -> str:
        return self.name

# owl carosel images for 4 fields


# ooty


class ooty_packages(models.Model):
    image = models.ImageField(upload_to="upload_photos", null=False)
    video = models.FileField(upload_to="upload_videous",
                             null=True, blank=True)  # FileField-videous
    title = models.CharField(max_length=100)
    discription = models.TextField(null=False)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title


# coonoor


class coonoor_packages(models.Model):
    image = models.ImageField(upload_to="upload_photos", null=False)
    video = models.FileField(upload_to="upload_videous",
                             null=True, blank=True)  # FileField-videous
    title = models.CharField(max_length=100)
    discription = models.TextField(null=False)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title


# manjoor
class manjoor_packages(models.Model):
    image = models.ImageField(upload_to="upload_photos", null=False)
    video = models.FileField(upload_to="upload_videous",
                             null=True, blank=True)  # FileField-videous
    title = models.CharField(max_length=100)
    discription = models.TextField(null=False)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title


# masinagudi
class masinagudi_packages(models.Model):
    image = models.ImageField(upload_to="upload_photos", null=False)
    video = models.FileField(upload_to="upload_videous",
                             null=True, blank=True)  # FileField-videous
    title = models.CharField(max_length=100)
    discription = models.TextField(null=False)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

# combo packages


class owl_combo_packages(models.Model):
    image = models.ImageField(upload_to="upload_photos", null=False)
    title = models.CharField(max_length=100)
    places = models.CharField(max_length=200)
    discription = models.CharField(max_length=250, null=False)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


# all packages


class packages(models.Model):
    image = models.ImageField(upload_to="upload_photos", null=False)
    video = models.FileField(upload_to="upload_videous",
                             null=True, blank=True)  # FileField-videous
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=250, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
