# Generated by Django 4.2.7 on 2023-11-21 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0007_rename_type_of_deel_property_type_of_deal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='type_of_deal',
            field=models.CharField(choices=[('SALE', 'SALE'), ('RENT', 'RENT')], default='SALE', max_length=10),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='my_site.property')),
            ],
        ),
    ]
