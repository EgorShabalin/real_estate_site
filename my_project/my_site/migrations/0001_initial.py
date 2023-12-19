# Generated by Django 4.2.7 on 2023-12-19 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('APARTMENT', 'Apartment'), ('COMMERS', 'Commercial unit'), ('LAND', 'Land'), ('BUILDING', 'Building'), ('FARM HOUSE', 'Farm house'), ('UNDER CONSTRUCTION', 'Under construction')], default='APARTMENT', max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Heating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('NO', 'No Heating'), ('AC', 'Air Conditioner heating'), ('GAS', 'Natural Gas heating'), ('STOVE', 'Fire Place heating'), ('ELECTRIC', 'Electric Boiler heating')], default='NO', max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Heating types',
            },
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_type', models.CharField(choices=[('PARKING ON THE STREET', 'STREET'), ('PARKING ON SITE', 'ON SITE'), ('ROOFED PARKING ON SITE', 'ROOFED ON SITE'), ('UNDERGROUND PARKING', 'UNDERGROUND')], default='PARKING ON THE STREET', max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Parking types',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('province', models.CharField(choices=[('Ağrı', 'Ağrı'), ('Adana', 'Adana'), ('Adıyaman', 'Adıyaman'), ('Aydın', 'Aydın'), ('Aksaray', 'Aksaray'), ('Amasya', 'Amasya'), ('Ankara', 'Ankara'), ('Antalya', 'Antalya'), ('Ardahan', 'Ardahan'), ('Artvin', 'Artvin'), ('Afyonkarahisar', 'Afyonkarahisar'), ('Bayburt', 'Bayburt'), ('Balıkesir', 'Balıkesir'), ('Bartın', 'Bartın'), ('Batman', 'Batman'), ('Bilecik', 'Bilecik'), ('Bingöl', 'Bingöl'), ('Bitlis', 'Bitlis'), ('Bolu', 'Bolu'), ('Burdur', 'Burdur'), ('Bursa', 'Bursa'), ('Van', 'Van'), ('Gaziantep', 'Gaziantep'), ('Giresun', 'Giresun'), ('Gümüşhane', 'Gümüşhane'), ('Denizli', 'Denizli'), ('Diyarbakır', 'Diyarbakır'), ('Düzce', 'Düzce'), ('Zonguldak', 'Zonguldak'), ('İzmir', 'İzmir'), ('Yozgat', 'Yozgat'), ('Kayseri', 'Kayseri'), ('Karabük', 'Karabük'), ('Karaman', 'Karaman'), ('Kars', 'Kars'), ('Kastamonu', 'Kastamonu'), ('Kahramanmaraş', 'Kahramanmaraş'), ('Kilis', 'Kilis'), ('Kocaeli', 'Kocaeli'), ('Konya', 'Konya'), ('Kırklareli', 'Kırklareli'), ('Kırşehir', 'Kırşehir'), ('Kırıkkale', 'Kırıkkale'), ('Kütahya', 'Kütahya'), ('Malatya', 'Malatya'), ('Manisa', 'Manisa'), ('Mardin', 'Mardin'), ('Mersin', 'Mersin'), ('Muğla', 'Muğla'), ('Muş', 'Muş'), ('Nevşehir', 'Nevşehir'), ('Niğde', 'Niğde'), ('Ordu', 'Ordu'), ('Osmaniye', 'Osmaniye'), ('Rize', 'Rize'), ('Sakarya', 'Sakarya'), ('Samsun', 'Samsun'), ('Sivas', 'Sivas'), ('Siirt', 'Siirt'), ('Sinop', 'Sinop'), ('İstanbul', 'İstanbul'), ('Tekirdağ', 'Tekirdağ'), ('Tokat', 'Tokat'), ('Trabzon', 'Trabzon'), ('Tunceli', 'Tunceli'), ('Uşak', 'Uşak'), ('Hakkâri', 'Hakkâri'), ('Hatay', 'Hatay'), ('Çanakkale', 'Çanakkale'), ('Çankırı', 'Çankırı'), ('Çorum', 'Çorum'), ('Şanlıurfa', 'Şanlıurfa'), ('Şırnak', 'Şırnak'), ('Iğdır', 'Iğdır'), ('Isparta', 'Isparta'), ('Edirne', 'Edirne'), ('Elazığ', 'Elazığ'), ('Erzincan', 'Erzincan'), ('Erzurum', 'Erzurum'), ('Eskişehir', 'Eskişehir'), ('Yalova', 'Yalova')], default='Antalya', max_length=50)),
                ('district', models.CharField(blank=True, choices=[('Akseki', 'Akseki'), ('Aksu', 'Aksu'), ('Alanya', 'Alanya'), ('Demre', 'Demre'), ('Döşemealtı', 'Döşemealtı'), ('Elmalı', 'Elmalı'), ('Finike', 'Finike'), ('Gazipaşa', 'Gazipaşa'), ('Gündoğmuş', 'Gündoğmuş'), ('İbradı', 'İbradı'), ('Kaş', 'Kaş'), ('Kemer', 'Kemer'), ('Kepez', 'Kepez'), ('Konyaaltı', 'Konyaaltı'), ('Korkuteli', 'Korkuteli'), ('Kumluca', 'Kumluca'), ('Manavgat', 'Manavgat'), ('Muratpaşa', 'Muratpaşa'), ('Serik', 'Serik')], max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('floor_number', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('total_floors', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('rooms', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('type_of_deal', models.CharField(choices=[('SALE', 'SALE'), ('RENT', 'RENT')], default='SALE', max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default=[1], on_delete=django.db.models.deletion.CASCADE, to='my_site.category')),
                ('heating', models.ForeignKey(default=[1], on_delete=django.db.models.deletion.CASCADE, to='my_site.heating')),
                ('parking', models.ForeignKey(default=[1], on_delete=django.db.models.deletion.CASCADE, to='my_site.parking')),
            ],
            options={
                'verbose_name_plural': 'Emlak listesi | Property list',
                'ordering': ('-created_at',),
            },
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
