# Generated by Django 4.0.2 on 2022-04-21 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_orderitem_order_remove_orderitem_product_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]