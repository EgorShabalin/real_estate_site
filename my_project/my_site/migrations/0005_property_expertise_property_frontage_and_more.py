# Generated by Django 4.2.7 on 2023-12-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0004_alter_property_elevator'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='expertise',
            field=models.CharField(blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], default='YES', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='frontage',
            field=models.CharField(blank=True, choices=[('North', 'North'), ('East', 'East'), ('South', 'South'), ('West', 'West'), ('North-East', 'North-East'), ('South-East', 'South-East'), ('South-West', 'South-West'), ('North-West', 'North-West')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='residence_permit',
            field=models.CharField(blank=True, choices=[('Possible', 'Possible'), ('Not possible', 'Not possible')], default='Not possible', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='tapu',
            field=models.CharField(blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], default='YES', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Apartment', 'Apartment'), ('Commercial unit', 'Commercial unit'), ('Land', 'Land'), ('Building', 'Building'), ('Farm house', 'Farm house'), ('Under construction', 'Under construction')], default='APARTMENT', max_length=25),
        ),
        migrations.AlterField(
            model_name='heating',
            name='type',
            field=models.CharField(choices=[('No heating', 'No Heating'), ('Air Conditioner heating', 'Air Conditioner heating'), ('Natural Gas heating', 'Natural Gas heating'), ('Geothermal', 'Geothermal'), ('Fire Place heating', 'Fire Place heating'), ('Electric Boiler heating', 'Electric Boiler heating')], default='NO', max_length=25),
        ),
        migrations.AlterField(
            model_name='parking',
            name='type',
            field=models.CharField(choices=[('Parking on the street', 'STREET'), ('Parking on site', 'ON SITE'), ('Roofed parking on site', 'ROOFED ON SITE'), ('Underground parking', 'UNDERGROUND')], default='PARKING ON THE STREET', max_length=25),
        ),
    ]
