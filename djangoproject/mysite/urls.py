from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('ecom/', include('ecomm.urls')),
    path('shopping/', include('shopingcart.urls')),
    path('shopingcart/', include('shopingcart.urls')),
 
]
