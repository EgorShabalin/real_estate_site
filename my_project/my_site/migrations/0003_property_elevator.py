# Generated by Django 4.2.7 on 2023-12-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0002_rename_parking_type_parking_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='elevator',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], default='Antalya', max_length=50),
        ),
    ]
