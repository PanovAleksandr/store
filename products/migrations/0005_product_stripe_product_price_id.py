# Generated by Django 3.2.13 on 2023-02-24 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20230201_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_product_price_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
