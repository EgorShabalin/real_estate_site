# Generated by Django 4.2.7 on 2024-07-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0023_blog_en_text_blog_en_title_blog_ru_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='de_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='de_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
