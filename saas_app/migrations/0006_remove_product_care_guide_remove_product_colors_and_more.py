# Generated by Django 5.1.3 on 2024-12-01 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saas_app', '0005_facility_description_facility_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='care_guide',
        ),
        migrations.RemoveField(
            model_name='product',
            name='colors',
        ),
        migrations.RemoveField(
            model_name='product',
            name='delivery_info',
        ),
        migrations.RemoveField(
            model_name='product',
            name='materials',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sizes',
        ),
        migrations.AlterField(
            model_name='facility',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Изображение'),
        ),
    ]
