# Generated by Django 4.2.7 on 2023-12-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0006_remove_property_tapu_property_iskan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]
