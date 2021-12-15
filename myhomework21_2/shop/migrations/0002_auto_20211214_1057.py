# Generated by Django 3.2.10 on 2021-12-14 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='desctiption',
            new_name='description',
        ),
        migrations.AddField(
            model_name='shop',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
            preserve_default=False,
        ),
    ]
