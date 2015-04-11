# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField()),
                ('last_update', models.DateTimeField()),
                ('latitude', models.DecimalField(max_digits=8, decimal_places=6)),
                ('longitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('event_type', models.CharField(max_length=20, choices=[(b'climate', b'Climate'), (b'pollution', b'Pollution'), (b'depletion', b'Depletion')])),
                ('author', models.ForeignKey(to='app.IzumiUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField()),
                ('last_update', models.DateTimeField()),
                ('latitude', models.DecimalField(max_digits=8, decimal_places=6)),
                ('longitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('source_type', models.CharField(max_length=20, choices=[(b'surface', b'Surface'), (b'ground', b'Ground'), (b'frozen', b'Frozen'), (b'other', b'Other')])),
                ('pathogen_pollution', models.IntegerField()),
                ('inorganic_pollution', models.IntegerField()),
                ('organic_pollution', models.IntegerField()),
                ('macroscopic_pollution', models.IntegerField()),
                ('thermal_pollution', models.IntegerField()),
                ('author', models.ForeignKey(to='app.IzumiUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
