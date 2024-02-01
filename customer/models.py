from django.db import models


from users.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'customer_customer'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'
        ordering = ["-id"]

    def __str__(self):
        return self.user.phone_number


class Slider(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="slideshow")


    class Meta:
        db_table = 'slideshow_image'
        verbose_name = 'slider'
        verbose_name_plural = 'slide'
        ordering = ["-id"]

    def __str__(self):
        return self.name
    






   