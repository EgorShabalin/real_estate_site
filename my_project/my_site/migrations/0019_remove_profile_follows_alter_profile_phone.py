# Generated by Django 4.2.7 on 2024-01-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0018_alter_profile_phone_alter_team_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follows',
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
