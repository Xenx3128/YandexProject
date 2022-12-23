# Generated by Django 3.2.16 on 2022-12-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20221215_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friends',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='254 symbols max', max_length=254, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, help_text='127 symbols max', max_length=127, null=True, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, help_text='127 symbols max', max_length=127, null=True, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='127 symbols max', max_length=127, verbose_name='username'),
        ),
    ]