from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'price', 'availability', 'slug', 'created', 'update']
    list_filter = ['availability', 'created', 'update']
    list_editable = ['price', 'availability']
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug':('name',)}