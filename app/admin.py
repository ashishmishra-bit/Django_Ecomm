from django.contrib import admin
from .models import (
    Customer, 
    Product,
    Cart,
    OrderPlaced
)
# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id' , 'user' , 'name' , 'locality' , 'city' , 'state' , 'zipcode']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id' ,'title' , 'description' , 'selling_price' , 'discounted_price' , 'category' , 'brand', 'product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id' , 'product' , 'quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id' , 'user' , 'customer' , 'product' , 'quantity' , 'ordered_date' , 'status']

