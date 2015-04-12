# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150404_1915'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField()),
                ('d_pathogen_pollution', models.DecimalField(default=0, max_digits=4, decimal_places=1)),
                ('d_inorganic_pollution', models.DecimalField(default=0, max_digits=4, decimal_places=1)),
                ('d_organic_pollution', models.DecimalField(default=0, max_digits=4, decimal_places=1)),
                ('d_macroscopic_pollution', models.DecimalField(default=0, max_digits=4, decimal_places=1)),
                ('d_thermal_pollution', models.DecimalField(default=0, max_digits=4, decimal_places=1)),
                ('d_depletion_risk', models.DecimalField(default=0, max_digits=4, decimal_places=1)),
                ('d_climate_condition', models.DecimalField(default=0, max_digits=4, decimal_places=1)),
                ('d_stress', models.DecimalField(default=0, max_digits=4, decimal_places=1)),
                ('author', models.ForeignKey(to='app.IzumiUser')),
                ('source_id', models.ForeignKey(to='api.Source')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='event',
            name='author',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='last_update',
            new_name='last_updated',
        ),
        migrations.AddField(
            model_name='source',
            name='climate_condition',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='source',
            name='depletion_risk',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='source',
            name='stress',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='source',
            name='inorganic_pollution',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='source',
            name='macroscopic_pollution',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='source',
            name='organic_pollution',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='source',
            name='pathogen_pollution',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='source',
            name='thermal_pollution',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=1),
            preserve_default=True,
        ),
    ]
