# Generated by Django 5.0 on 2023-12-28 08:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now=True)),
                ('ordered', models.BooleanField(default=False)),
                ('qty', models.IntegerField(default=1)),
                ('amount', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'order cart',
                'verbose_name_plural': 'order carts',
                'db_table': 'customer_order_cart',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('pincode', models.FloatField()),
                ('amount', models.FloatField()),
                ('status', models.CharField(choices=[('pending', 'pending'), ('packed', 'packed'), ('shipped', 'shipped'), ('delivered', 'delivered')], max_length=25)),
                ('is_paid', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('items', models.ManyToManyField(related_name='item', to='order.orderitem')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'db_table': 'customer_order',
                'ordering': ['-id'],
            },
        ),
    ]
