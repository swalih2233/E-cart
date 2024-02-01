from django.db import models


from users.models import User
from product.models import Product
from customer.models import Customer




ORDER_STATUS_CHOICES = (
    ("pending","pending"),
    ("packed","packed"),
    ("shipped","shipped"),
    ("delivered","delivered")

)

class Orderitem(models.Model):
    created_date = models.DateField(auto_now=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    qty = models.IntegerField(default=1)
    amount = models.FloatField()


    class Meta:
        db_table = 'customer_order_cart'
        verbose_name = 'order cart'
        verbose_name_plural = 'order carts'
        ordering = ('id',)

    def __str__(self):

        return self.product.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Orderitem, related_name='item')
    address = models.TextField()
    pincode = models.FloatField()
    amount = models.FloatField()
    status = models.CharField(max_length=25, choices=ORDER_STATUS_CHOICES)
    is_paid = models.BooleanField(default=False)

    class Meta:
        db_table ='customer_order'
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        ordering = ["-id"]

    def __str__(self):
        return self.customer.user.first_name
