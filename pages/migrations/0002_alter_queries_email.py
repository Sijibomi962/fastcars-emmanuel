# Generated by Django 4.0.6 on 2022-08-08 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queries',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
