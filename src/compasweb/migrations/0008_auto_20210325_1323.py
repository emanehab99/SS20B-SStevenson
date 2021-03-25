# Generated by Django 2.2.14 on 2021-03-25 02:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compasweb', '0007_auto_20210210_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compasmodelrun',
            name='orbital_period',
            field=models.FloatField(blank=True, help_text='Value > 0', null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='separation',
            field=models.FloatField(blank=True, help_text='Value > 0', null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
