# Generated by Django 4.2.6 on 2023-11-02 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_gallry_photo_gallery_gallery_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='gallery_photo',
        ),
    ]
