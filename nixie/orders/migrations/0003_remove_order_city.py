# Generated by Django 4.1.6 on 2023-04-18 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orderitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
    ]
