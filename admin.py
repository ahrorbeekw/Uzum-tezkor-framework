from django.contrib import admin
from .models import Category, Restorantlar, Mahsulotlar

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  
    search_fields = ('name',)  

# Restoranlar uchun admin interfeysi
@admin.register(Restorantlar)
class RestorantlarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_id', 'created_time')  
    list_filter = ('category_id',)  
    search_fields = ('name',)  
    ordering = ('-created_time',)  
    autocomplete_fields = ('category_id',)

# Mahsulotlar uchun admin interfeysi
@admin.register(Mahsulotlar)
class MahsulotlarAdmin(admin.ModelAdmin):
    list_display = ('id', 'mahsulot_name', 'mahsulot_narx',  'mahsulot_body', 'restorant_id', 'created_time') 
    list_filter = ('restorant_id',)  
    search_fields = ('mahsulot_name',)  
    ordering = ('-created_time',) 
    autocomplete_fields = ('restorant_id',)  
