# Generated by Django 4.1.6 on 2023-04-08 22:02

from django.db import migrations, models
import nixie_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('nixie_app', '0005_alter_product_image1_alter_product_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Доступно'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создано'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, upload_to=nixie_app.models.upload_photo_to, verbose_name='Главная картинка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, upload_to=nixie_app.models.upload_photo_to, verbose_name='Картинка №2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, upload_to=nixie_app.models.upload_photo_to, verbose_name='Картинка №3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='lamp_currency',
            field=models.CharField(blank=True, choices=[('4', '4'), ('6', '6')], db_index=True, max_length=1, null=True, verbose_name='Кол-во ламп'),
        ),
        migrations.AlterField(
            model_name='product',
            name='lamp_type',
            field=models.CharField(blank=True, choices=[('ИН-8', 'ИН-8'), ('ИН-12', 'ИН-12'), ('ИН-14', 'ИН-14'), ('ИН-16', 'ИН-16'), ('ИН-17', 'ИН-17'), ('ИН-18', 'ИН-18')], db_index=True, max_length=10, null=True, verbose_name='Тип ламп'),
        ),
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(verbose_name='Наличие'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Изменено'),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Ширина'),
        ),
    ]