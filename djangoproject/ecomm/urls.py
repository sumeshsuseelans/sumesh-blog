from django.urls import path
from . import views

urlpatterns = [
    path('', views.Ecomhome, name='Ecomhome'),
    path('johnOrder', views.JohnOrder, name='JohnOrder'),
    path('contgect_page', views.contgect_page, name='contgect_page'),
]
