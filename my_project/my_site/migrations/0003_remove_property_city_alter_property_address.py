# Generated by Django 4.2.7 on 2023-11-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0002_remove_category_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='city',
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
