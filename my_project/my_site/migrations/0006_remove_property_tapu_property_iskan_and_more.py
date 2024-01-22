# Generated by Django 4.2.7 on 2023-12-22 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0005_property_expertise_property_frontage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='tapu',
        ),
        migrations.AddField(
            model_name='property',
            name='iskan',
            field=models.CharField(blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], default='Yes', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Apartment', 'Apartment'), ('Commercial unit', 'Commercial unit'), ('Land', 'Land'), ('Building', 'Building'), ('Farm house', 'Farm house'), ('Under construction', 'Under construction')], default='Apartment', max_length=25),
        ),
        migrations.AlterField(
            model_name='heating',
            name='type',
            field=models.CharField(choices=[('No heating', 'No Heating'), ('Air Conditioner heating', 'Air Conditioner heating'), ('Natural Gas heating', 'Natural Gas heating'), ('Geothermal', 'Geothermal'), ('Fire Place heating', 'Fire Place heating'), ('Electric Boiler heating', 'Electric Boiler heating')], default='No heating', max_length=25),
        ),
        migrations.AlterField(
            model_name='parking',
            name='type',
            field=models.CharField(choices=[('Parking on the street', 'Parking on the street'), ('Parking on site', 'Parking on site'), ('Roofed parking on site', 'Roofed parking on site'), ('Underground parking', 'Underground parking')], default='Parking on the street', max_length=25),
        ),
        migrations.AlterField(
            model_name='property',
            name='elevator',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], default='No', max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='expertise',
            field=models.CharField(blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], default='Yes', max_length=50, null=True),
        ),
    ]