from django.contrib import admin
from .models import *

# Register your models here.

class OrderProductInline (admin.TabularInline):
    model=OrderProduct
    readonly_fields=['user','product','quantity','product_price']
    extra=0

class OrderAdmin (admin.ModelAdmin):
    list_display=['order_numper','full_name','phone','email','order_total','tax','payment_method','is_order','created_at']
    list_filter=['payment_method','is_order']
    search_fields=['order_numper','first_name','last_name','phone','email']
    list_per_page=20
    inlines=[OrderProductInline]



admin.site.register(Order,OrderAdmin)
admin.site.register(Payment)
