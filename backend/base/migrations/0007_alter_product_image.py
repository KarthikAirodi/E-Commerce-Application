# Generated by Django 4.1.4 on 2023-01-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='React-App_5.png', null=True, upload_to=''),
        ),
    ]
