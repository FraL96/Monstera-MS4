from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'category',
        'name',
        'species',
        'price',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
