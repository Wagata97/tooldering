from django.contrib import admin
from orders.models import Associates, Orders


@admin.register(Associates)
class AssociatesAmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'associate', 'product', 'price', 'currency', 'status']
    list_filter = ['associate', 'status']
