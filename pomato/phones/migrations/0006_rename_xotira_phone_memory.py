# Generated by Django 4.0.4 on 2022-06-10 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0005_alter_brand_image_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='xotira',
            new_name='memory',
        ),
    ]
