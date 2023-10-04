from django.db import models

# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=100)
    cimage = models.ImageField(upload_to='data',default='null.jpg')
    cdescription = models.CharField(max_length=100)
    
class Product(models.Model):
    pname = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to='data',default='null.jpg')
    price = models.IntegerField()
    quantity = models.IntegerField()
    status = models.IntegerField(default=0)
    stock = models.IntegerField(null=True)

    def __str__(self):
        return self.pname
    
