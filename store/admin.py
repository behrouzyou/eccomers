import admin_thumbnails
from django.contrib import admin

from .models import Product, ProductGallery, Variation


# Register your models here.
@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'is_available','modified_date')
    prepopulated_fields = {'slug': ('product_name',)}  # noqa: RUF012
    inlines = [ProductGalleryInline]  # noqa: RUF012

@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value','is_active','created_date')
    list_editable = ('is_active',)
    list_filter = ('product','variation_category')
    
    
    
admin.site.register(ProductGallery)