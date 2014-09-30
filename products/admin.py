from django.contrib import admin

from products.models import Product, Cost

class CostInline(admin.TabularInline):
    model = Cost

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        CostInline,
    ]

admin.site.register(Product, ProductAdmin)
