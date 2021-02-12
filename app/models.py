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
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('Pending', 'Pending'),
    ('On The Way', 'On The Way'),
    ('Delivered','Delivered'),
    ('Cancel', 'Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DataTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,
    choices=STATE_CHOICES,default='Pending')


    