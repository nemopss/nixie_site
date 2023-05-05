# Generated by Django 4.1.6 on 2023-04-08 21:58

from django.db import migrations, models
import nixie_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('nixie_app', '0004_remove_product_category_remove_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, upload_to=nixie_app.models.upload_photo_to),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, upload_to=nixie_app.models.upload_photo_to),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, upload_to=nixie_app.models.upload_photo_to),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(blank=True, choices=[('Ясень', 'Ясень'), ('Дуб', 'Дуб'), ('Бук', 'Бук')], db_index=True, max_length=50, null=True, verbose_name='Материал'),
        ),
    ]
