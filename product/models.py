from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=25)
    image =models.ImageField(upload_to='category')


    class Meta:
        db_table = 'products_category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ["-id"]

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="subcategory")
    parent = models.ForeignKey(Category, on_delete=models.CASCADE)


    class Meta:
        db_table = 'product_subcategory'
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    category =models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE,null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="products")
    is_stock = models.BooleanField(default=True)


    class Meta:
        db_table = 'products_product'
        verbose_name ='product'
        verbose_name_plural = 'products'
        ordering = ["-id"]

    def __str__(self):
        return self.name