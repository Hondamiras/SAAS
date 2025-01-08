from django.contrib import admin
from .models import AboutUs, Facility, News, Category, Product, ProductImage, FacilityImages
from django.utils.safestring import mark_safe

# Admin for AboutUs
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_published', 'time_create', 'time_update')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')
    list_editable = ('is_published',)

# Admin for Facility
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}

class FacilityImagesAdmin(admin.ModelAdmin):
    list_display = ('facility', 'image')

# Admin for News
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}

# Admin for Category
@admin.register(Category)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

# Admin for Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}

    def formatted_description(self, obj):
        return mark_safe(obj.description)

    formatted_description.short_description = 'Description'

# Admin for ProductImage
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')

# Register other models without decorators
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(FacilityImages, FacilityImagesAdmin)
