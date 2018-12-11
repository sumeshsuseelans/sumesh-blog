from django.contrib import admin
from .models import Register
from .models import Cart
from .models import Items

admin.site.register(Register)
admin.site.register(Cart)
admin.site.register(Items)