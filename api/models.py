from django.db import models
from django.contrib import admin
from app.models import IzumiUser

# Create your models here.

class Source(models.Model):
    SOURCE_CHOICES = (
        ('surface', 'Surface'),
        ('ground', 'Ground'),
        ('frozen', 'Frozen'),
        ('other', 'Other'),
    )

    author = models.ForeignKey(IzumiUser)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    source_type = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    pathogen_pollution = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    inorganic_pollution = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    organic_pollution = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    macroscopic_pollution = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    thermal_pollution = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    depletion_risk = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    climate_condition = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    stress = models.DecimalField(max_digits=4, decimal_places=1, default=0)

class History(models.Model):
    source_id = models.ForeignKey(Source)
    author = models.ForeignKey(IzumiUser)
    date_created = models.DateTimeField()
    latitude = models.DecimalField(max_digits=8, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    d_pathogen_pollution = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    d_inorganic_pollution = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    d_organic_pollution = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    d_macroscopic_pollution = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    d_thermal_pollution = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    d_depletion_risk = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    d_climate_condition = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    d_stress = models.DecimalField(max_digits=4, decimal_places=1, default=0)
