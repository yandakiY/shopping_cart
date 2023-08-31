from django.contrib import admin
from .models import Product , Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'display_image', 'display_categories')
    readonly_fields = ('display_image', 'display_categories')

    def display_image(self, obj):
        return obj.image.url if obj.image else None
    display_image.short_description = 'Image'

    def display_categories(self, obj):
        return ', '.join([category.name for category in obj.category.all()])
    display_categories.short_description = 'Categories'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)