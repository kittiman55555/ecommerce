# Generated by Django 2.2 on 2019-04-18 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(default=1, upload_to='products/'),
            preserve_default=False,
        ),
    ]