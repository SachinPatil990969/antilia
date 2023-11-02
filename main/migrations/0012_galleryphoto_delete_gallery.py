# Generated by Django 4.2.6 on 2023-11-02 09:21

import authentication.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_gallery_gallery_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='galleryphoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gallery_photo', models.FileField(upload_to=authentication.helpers.custom_file_name)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='gallery',
        ),
    ]
