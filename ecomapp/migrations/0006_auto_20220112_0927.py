# Generated by Django 3.1 on 2022-01-12 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Card', 'Card'), ('Online Payment', 'Online Payment')], default='Cash On Delivery', max_length=20),
        ),
    ]
