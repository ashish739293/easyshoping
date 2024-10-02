# Generated by Django 4.1 on 2022-09-03 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ossapp', '0030_alter_shoppingcart_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='customer',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ossapp.product'),
        ),
    ]
