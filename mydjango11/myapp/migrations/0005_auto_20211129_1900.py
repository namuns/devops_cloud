# Generated by Django 3.2.9 on 2021-11-29 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_item_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='gift',
        ),
        migrations.RemoveField(
            model_name='item',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
    ]
