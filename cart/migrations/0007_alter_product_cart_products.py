# Generated by Django 3.2.12 on 2023-08-12 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_vendor'),
        ('cart', '0006_alter_product_cart_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_cart',
            name='products',
            field=models.ManyToManyField(to='inventory.Product'),
        ),
    ]
