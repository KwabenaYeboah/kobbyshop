# Generated by Django 3.1 on 2021-11-30 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20211130_0743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='customer',
            new_name='order',
        ),
    ]
