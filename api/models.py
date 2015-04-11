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
    last_update = models.DateTimeField()
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    source_type = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    pathogen_pollution = models.IntegerField()
    inorganic_pollution = models.IntegerField()
    organic_pollution = models.IntegerField()
    macroscopic_pollution = models.IntegerField()
    thermal_pollution = models.IntegerField()

class Event(models.Model):
    MAIN_EVENT_CHOICES = (
        ('climate', 'Climate'),
        ('pollution', 'Pollution'),
        ('depletion', 'Depletion'),
    )

    author = models.ForeignKey(IzumiUser)
    date_created = models.DateTimeField()
    last_update = models.DateTimeField()
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    event_type = models.CharField(max_length=20, choices=MAIN_EVENT_CHOICES)
