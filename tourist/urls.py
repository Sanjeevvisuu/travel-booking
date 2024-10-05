

from django.contrib import admin
from django.urls import path,include
from website_app.urls import *
from product.urls import *
from about_us.urls import *
from payment.urls import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("website_app.urls")),
    path("product",include("product.urls")),
    path("booking",include("booking.urls")),
    path("contact",include("contact.urls")),
    path("about",include("about_us.urls")),
    path("payment",include("payment.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
