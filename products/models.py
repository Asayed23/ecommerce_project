from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(null=True,blank=True)
    image1 = models.TextField(null=True,blank=True)
    image2 = models.TextField(null=True,blank=True)
    image3 = models.TextField(null=True,blank=True)
    image4 = models.TextField(null=True,blank=True)
    image5 = models.TextField(null=True,blank=True)
    image6 = models.TextField(null=True,blank=True)
    image7 = models.TextField(null=True,blank=True)
    image8 = models.TextField(null=True,blank=True)
    image9 = models.TextField(null=True,blank=True)
    image10 = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('Product', through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.product.title} in {self.cart}"
