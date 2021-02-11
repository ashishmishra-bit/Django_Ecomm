from django.db import models

# Create your models here. 
'''class Profile(models.Model):
    name = models.CharField(max_length=30)    
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=6)'''

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    #product_price = models.IntegerField()
    product_category = models.CharField(max_length=50)
    product_description = models.CharField(max_length=1000)



    