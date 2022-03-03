from django.contrib import admin

# Register your models here.
from .models import Cart,Product,CartProduct,Category,Favorire,Order


admin.site.register([Cart,Product,CartProduct,Category,Favorire,Order])