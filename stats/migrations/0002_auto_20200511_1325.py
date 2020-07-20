# Generated by Django 3.0.6 on 2020-05-11 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='attack',
        ),
        migrations.RemoveField(
            model_name='data',
            name='defense',
        ),
        migrations.AddField(
            model_name='data',
            name='attack_type',
            field=models.CharField(default='basic', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='region',
            field=models.CharField(default='rift', max_length=200),
            preserve_default=False,
        ),
    ]
