from itertools import product
from django.contrib import admin
from . import models
from django import forms





@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name','customer_code','category','address','place',]
    list_per_page = 10
    search_fields = ['customer_name__istartswith','customer_code__iendswith']
   
       

# admin.site.register(models.Item) 
@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields=['our_item_code__istartswith']
    list_display = ['our_item_code','item_name']
    list_per_page = 10


@admin.register(models.Uom)
class UomAdmin(admin.ModelAdmin):

    list_display= ['unit','unit_type','unit_code']    
   

class CustomerPoItemInline(admin.TabularInline):
    model = models.CustomerPoItem



@admin.register(models.CustomerPo)
class CustomerPoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer_name']  
    inlines = [CustomerPoItemInline]
    list_display = ['customer_po_number','date','customer_name','status',]
    list_editable = ['status']
    list_per_page = 10
    list_select_related = ['customer_name']
    search_fields = ['customer_po_number__istartswith','status__istartswith']

    def customer_address(self,customerpo):
        return customerpo.customer_name.address




@admin.register(models.CustomerPoItem)
class CustomerPoItemAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer_po_number']  
    list_display = ['customer_po_number','customer_name','customer_item_code','customer_item_description','quantity','unit',]
    list_per_page = 10
    list_select_related = ['customer_po_number','unit']

    # def name(self, obj):
    #     obj.content=f"Hello{obj.id}"
    #     return obj.content

    def customer_name(self,customerpoitem):
        return customerpoitem.customer_po_number.customer_name

   
