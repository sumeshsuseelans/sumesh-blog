from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about-us', views.about, name='about'),
    path('contact-us', views.contact, name='contact'),
    path('items', views.items, name='items'),
    path('order', views.order, name='order'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('cross_off/<list_id>', views.cross_off, name='cross_off'),
    path('uncross/<list_id>', views.uncross, name='uncross'),
    path('edit/<list_id>', views.edit, name='edit'),
    path('books', views.books, name='books'),
    path('movies', views.movies, name='movies'),


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)