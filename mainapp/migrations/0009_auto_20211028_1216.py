# Generated by Django 3.2.7 on 2021-10-28 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_customer_algo_private_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='driver_license',
            field=models.IntegerField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='home_address',
            field=models.CharField(max_length=500, null=True),
        ),
    ]