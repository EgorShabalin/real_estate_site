# Generated by Django 4.2.7 on 2024-02-28 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0020_alter_property_active_alter_property_address_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]