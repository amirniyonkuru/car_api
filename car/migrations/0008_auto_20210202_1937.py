# Generated by Django 3.1.5 on 2021-02-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_auto_20210202_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='rating',
            field=models.ManyToManyField(blank=True, default=0, to='car.Rating'),
        ),
    ]
