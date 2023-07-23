from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES=[
    ('milk','Milk'),
    ('curd','Curd'),
    ('milkshake','Milkshake'),
    ('paneer','Paneer'),
    ('sweets','Sweets'),
    ('buttermilk','Buttermilk'),
    ('ghee','Ghee'),
    ('lassi','Lassi'),
    ('icecream','Icecream')

]

STATE_CHOICES = [
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),
    ('Andaman and Nicobar','Andaman and Nicobar'),
    ('Chandigarh','Chandigarh'),
    ('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Lakshadweep','Lakshadweep'),
    ('Delhi','Delhi'),
    ('Puducherry','Puducherry'),
  
]
    


class Product(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=15)
    image=models.ImageField(upload_to='product')

    def __str__(self):
        return self.title

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    pincode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=30)
    mobileno=models.IntegerField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.price

    
