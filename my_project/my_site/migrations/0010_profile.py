# Generated by Django 4.2.7 on 2024-01-11 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_site', '0009_alter_property_bookmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ava', models.ImageField(blank=True, default=None, null=True, upload_to='avatars')),
                ('bio', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('current_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('follows', models.ManyToManyField(blank=True, related_name='followed_by', to='my_site.profile')),
            ],
        ),
    ]
