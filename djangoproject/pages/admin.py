from django.contrib import admin
from .models import List
from .models import Books
from .models import MoviesList

admin.site.register(List)
admin.site.register(Books)
admin.site.register(MoviesList)

