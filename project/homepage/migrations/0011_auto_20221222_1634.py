# Generated by Django 3.2.16 on 2022-12-22 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_auto_20221222_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proglanguage',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='slug',
        ),
    ]
