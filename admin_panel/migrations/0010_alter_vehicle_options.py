# Generated by Django 4.0.6 on 2022-08-17 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0009_remove_brand_brand_logo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'ordering': ('-brand',)},
        ),
    ]
