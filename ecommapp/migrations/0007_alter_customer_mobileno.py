# Generated by Django 4.2.3 on 2023-08-22 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0006_alter_customer_mobileno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobileno',
            field=models.IntegerField(max_length=12),
        ),
    ]
