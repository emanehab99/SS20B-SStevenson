# Generated by Django 2.2.14 on 2021-02-10 04:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compasweb', '0006_auto_20210111_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compasmodelrun',
            name='mean_anomaly',
        ),
        migrations.RemoveField(
            model_name='compasmodelrun',
            name='phi',
        ),
        migrations.RemoveField(
            model_name='compasmodelrun',
            name='seperation',
        ),
        migrations.RemoveField(
            model_name='compasmodelrun',
            name='theta',
        ),
        migrations.RemoveField(
            model_name='compasmodelrun',
            name='velocity',
        ),
        migrations.RemoveField(
            model_name='compasmodelrun',
            name='velocity_random_number',
        ),
        migrations.AddField(
            model_name='compasmodelrun',
            name='mean_anomaly_1',
            field=models.FloatField(blank=True, help_text='0 < Value < 2pi', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(6.283185307179586)]),
        ),
        migrations.AddField(
            model_name='compasmodelrun',
            name='mean_anomaly_2',
            field=models.FloatField(blank=True, help_text='0 < Value < 2pi', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(6.283185307179586)]),
        ),
        migrations.AddField(
            model_name='compasmodelrun',
            name='phi_1',
            field=models.FloatField(blank=True, help_text='0 < Value < 2pi', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(6.283185307179586)]),
        ),
        migrations.AddField(
            model_name='compasmodelrun',
            name='phi_2',
            field=models.FloatField(blank=True, help_text='0 < Value < 2pi', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(6.283185307179586)]),
        ),
        migrations.AddField(
            model_name='compasmodelrun',
            name='separation',
            field=models.FloatField(blank=True, help_text='Orbital separation of the binary. Value > 0', null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AddField(
            model_name='compasmodelrun',
            name='theta_1',
            field=models.FloatField(blank=True, help_text='0 < Value < 2pi', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(6.283185307179586)]),
        ),
        migrations.AddField(
            model_name='compasmodelrun',
            name='theta_2',
            field=models.FloatField(blank=True, help_text='0 < Value < 2pi', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(6.283185307179586)]),
        ),
        migrations.AddField(
            model_name='compasmodelrun',
            name='velocity_1',
            field=models.FloatField(blank=True, help_text=' Value > 0', null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AddField(
            model_name='compasmodelrun',
            name='velocity_2',
            field=models.FloatField(blank=True, help_text=' Value > 0', null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AddField(
            model_name='compasmodelrun',
            name='velocity_random_number_1',
            field=models.FloatField(blank=True, help_text='0 < Value < 1', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AddField(
            model_name='compasmodelrun',
            name='velocity_random_number_2',
            field=models.FloatField(blank=True, help_text='0 < Value < 1', null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='common_envelope_alpha',
            field=models.FloatField(default=1.0, help_text='Value > 0', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='common_envelope_lambda',
            field=models.FloatField(default=0.1, help_text='Value > 0', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='eccentricity',
            field=models.FloatField(default=0.0, help_text='Orbital eccentricity of the binary. 0 <= Value < 1', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='kick_velocity_sigma_CCSN_BH',
            field=models.FloatField(default=256.0, help_text='Value > 0', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='kick_velocity_sigma_CCSN_NS',
            field=models.FloatField(default=256.0, help_text='Value > 0', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='kick_velocity_sigma_ECSN',
            field=models.FloatField(default=30.0, help_text='Value > 0', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='kick_velocity_sigma_USSN',
            field=models.FloatField(default=30.0, help_text='Value > 0', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='mass1',
            field=models.FloatField(default=0.0, help_text='Mass of the initially more massive star.  0 < Value < 150', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(150.0)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='mass2',
            field=models.FloatField(default=0.0, help_text='Mass of the initially less massive star. 0 < Value < 150', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(150.0)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='max_time',
            field=models.FloatField(default=0, help_text='Maximum time to evolve binary for. 0 < Value <= 1400', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1400)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='maximum_neutron_star_mass',
            field=models.FloatField(default=2.5, help_text='Value > 0', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='metallicity',
            field=models.FloatField(default=0.0142, help_text='Metallicity of stars.  1E-4 < Value < 0.03', validators=[django.core.validators.MinValueValidator(0.0001), django.core.validators.MaxValueValidator(0.03)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='orbital_period',
            field=models.FloatField(blank=True, help_text='Orbital period of the binary. Value > 0', null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='pisn_lower_limit',
            field=models.FloatField(default=60.0, help_text='Value > 0', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='compasmodelrun',
            name='ppi_lower_limit',
            field=models.FloatField(default=35.0, help_text='Value > 0', validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]