from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'availability', 'slug', 'created', 'update']
    list_filter = ['availability', 'created', 'update']
    list_editable = ['price', 'availability']
    prepopulated_fields = {'slug':('name',)}