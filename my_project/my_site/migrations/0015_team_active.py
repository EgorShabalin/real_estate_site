# Generated by Django 4.2.7 on 2024-01-17 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0014_alter_team_ava'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
