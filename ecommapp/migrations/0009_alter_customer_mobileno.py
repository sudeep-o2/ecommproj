# Generated by Django 4.2.3 on 2023-08-22 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0008_alter_customer_mobileno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobileno',
            field=models.CharField(max_length=12),
        ),
    ]