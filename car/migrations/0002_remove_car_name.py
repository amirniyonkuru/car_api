# Generated by Django 3.1.5 on 2021-01-29 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='name',
        ),
    ]
