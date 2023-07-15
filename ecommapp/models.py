from django.db import models

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
    


class Product(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=15)
    image=models.ImageField(upload_to='product')

    def __str__(self):
        return self.title