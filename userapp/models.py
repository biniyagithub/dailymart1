from django.db import models
from adminapp.models import *
# Create your models here.
class Customer(models.Model):
    uname1 = models.CharField(max_length=100)
    uname2 = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)

class Contacts(models.Model):
    name = models.CharField(Customer,max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=100)

class Cart(models.Model):
    userid = models.ForeignKey(Customer,on_delete=models.CASCADE)
    productid = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0, null=True)
    status = models.IntegerField(default=0)

class Checkout(models.Model):
     userid = models.ForeignKey(Customer,on_delete=models.CASCADE)
     cartid = models.ForeignKey(Cart,on_delete=models.CASCADE)
     uname1 = models.CharField(max_length=100)
     uname2 = models.CharField(max_length=100)
     country = models.CharField(max_length=100)
     address = models.CharField(max_length=100)
     town = models.CharField(max_length=100)
     state = models.CharField(max_length=100)
     pincode = models.IntegerField()
     phone = models.IntegerField()
     email = models.EmailField()
     status = models.IntegerField(default=0)
     date = models.DateTimeField(auto_now_add=True,null=True)

class Buy(models.Model):
    userid = models.ForeignKey(Customer,on_delete=models.CASCADE)
    productid = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    address = models.CharField(max_length=100)
    pin = models.IntegerField()
    contact = models.IntegerField()
    status = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True,null=True)


class Order(models.Model):
    userid =models.ForeignKey(Customer,on_delete=models.CASCADE)
    cartid = models.ForeignKey(Cart,on_delete=models.CASCADE, null=True, blank=True)
    productid = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    status = models.IntegerField(default=0)
    total = models.IntegerField(default=0, null=True)
    quantity = models.IntegerField(default=0)


class Reset(models.Model):
    userid =models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,default=True)
    email1 = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True,null=True)




    


    
    
     
    