# Generated by Django 4.1 on 2022-08-07 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_messages_is_read_orders_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='is_read',
            field=models.BooleanField(verbose_name='Сообщение прочитано?'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.IntegerField(max_length=3, verbose_name='Статус заказа'),
        ),
    ]
