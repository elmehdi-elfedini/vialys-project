# products/admin.py
from django.contrib import admin
from .models import Product, Brand, Category, Order, Tag
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


admin.site.site_header = "Vialys Admin" 
admin.site.site_title = "Vialys Admin Portal"  
admin.site.index_title = "Bienvenue sur Vialys Admin Dashboard" 


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'quantity_in_stock', 'created_at', 'image_tag'] 
    search_fields = ['title', 'brand__name']  
    filter_horizontal = ['tags']  
    list_filter = ['brand', 'category', 'created_at'] 
    ordering = ['-created_at']  

    def image_tag(self, obj):
        if obj.image: 
            return format_html('<img src="{}" width="40" height="40" />', obj.image.url)  
        return "-"
    image_tag.short_description = _('Product Image')  



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'order_date', 'status']  
    search_fields = ['name', 'email'] 
    list_filter = ['order_date']
    ordering = ['-order_date']  
    actions = ['mark_as_shipped', 'mark_as_delivered', 'mark_as_canceled'] 

    def mark_as_shipped(self, request, queryset):
        queryset.update(status='Shipped')  # Marquer comme expédié
        self.message_user(request, _("Les commandes sélectionnées ont été marquées comme expédiées."))

    mark_as_shipped.short_description = _('Marquer les commandes sélectionnées comme expédiées.')

    def mark_as_delivered(self, request, queryset):
        queryset.update(status='Delivered')  # Marquer comme livré
        self.message_user(request, _("Les commandes sélectionnées ont été marquées comme livrées."))

    mark_as_delivered.short_description = _('Marquer les commandes sélectionnées comme livrées.')

    def mark_as_canceled(self, request, queryset):
        queryset.update(status='Canceled')  # Marquer comme annulé
        self.message_user(request, _("Les commandes sélectionnées ont été marquées comme annulées."))

    mark_as_canceled.short_description = _('Marquer les commandes sélectionnées comme annulées.')



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'category','image_tag']  
    search_fields = ['name']  
    list_filter = ['name', 'category']  
    
    def image_tag(self, obj):
        if obj.image:  
            return format_html('<img src="{}" width="80" height="30" />', obj.image.url)  
        return "-"
    image_tag.short_description = _('Brand Image') 



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name'] 
    search_fields = ['name']  
    list_filter = ['name']  


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']  
    search_fields = ['name', 'category']  
    list_filter = ['category']  
from django.contrib import admin
from .models import TeamMember
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'email', 'priority', 'image_tag']
    list_filter = ['role']
    search_fields = ['name', 'email']
    ordering = ['priority', 'name']

    def image_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.photo.url)
        return "-"
    image_tag.short_description = _('Photo')

    fieldsets = (
        ('Informations personnelles', {
            'fields': ('name', 'role', 'photo')
        }),
        ('Contact', {
            'fields': ('phone1', 'phone2', 'email')
        }),
        ('Configuration', {
            'fields': ('priority',)
        })
    )