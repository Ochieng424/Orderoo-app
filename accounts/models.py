from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=25, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=25, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    )
    name = models.CharField(max_length=25, null=True)
    price = models.FloatField()
    category = models.CharField(max_length=25, null=True, choices=CATEGORY)
    description = models.CharField(max_length=25, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    status = models.CharField(max_length=25, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, choices=STATUS)