from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    #list_display = ('id', 'brand', 'model', 'is_published', 'price', 'list_date', 'broker',)
    #list_display_links = ('id', 'model',)
    #list_filter = ('broker',)
    #list_editable = ('is_published',)
    #search_fields = ('brand', 'model', 'description', 'origin', 'price',)
    list_per_page = 25
    
admin.site.register(Listing, ListingAdmin)
