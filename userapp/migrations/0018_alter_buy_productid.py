# Generated by Django 4.2.4 on 2023-09-18 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_product_stock'),
        ('userapp', '0017_alter_buy_productid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='productid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.product'),
        ),
    ]