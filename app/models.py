from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here. 

STATE_CHOICES =(
    ('Andaman $ Nicobar' , 'Andaman $ Nicobar'),
    ('Andhra Pradesh' , 'Andhra Pradesh'),
    ('Arunachal Pradesh' , 'Arunachal Pradesh')
)
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)   
    locality = models.CharField(max_length=500)
    city = models.CharField(max_length=15)
    state = models.CharField(choices = STATE_CHOICES, max_length=50)
    zipcode = models.IntegerField()

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES =(
    ('M', 'Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW', 'Bottom Wear'),
)

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField()
    discount_price = models.FloatField()
    product_category = models.CharField(choices = CATEGORY_CHOICES , max_length=2)
    product_description = models.TextField(max_length=1000)
    product_brand = models.CharField(max_length=100)



    