# Generated by Django 5.1.3 on 2024-12-05 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saas_app', '0006_remove_product_care_guide_remove_product_colors_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]