# Generated by Django 3.2.9 on 2021-11-29 09:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='상품 번호')),
                ('category', models.CharField(max_length=20, verbose_name='카테고리')),
                ('name', models.CharField(max_length=20, verbose_name='상품명')),
                ('price', models.IntegerField(verbose_name='가격')),
                ('gift', models.BooleanField(default=0, verbose_name='포장여부')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='menus',
        ),
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now=True, verbose_name='주문 날짜'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.TextField(default=django.utils.timezone.now, max_length=100, verbose_name='주문 상품들'),
            preserve_default=False,
        ),
    ]
