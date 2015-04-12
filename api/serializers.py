from django.forms import widgets
from rest_framework import serializers
from api.models import Source, History

class SourceSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.user.username', read_only=True)
    class Meta:
        model = Source
        fields = (
            'id',
            'author',
            'date_created',
            'last_updated',
            'longitude',
            'latitude',
            'source_type',
            'pathogen_pollution',
            'inorganic_pollution',
            'organic_pollution',
            'macroscopic_pollution',
            'thermal_pollution',
            'climate_condition',
            'depletion_risk',
            'stress',
         )

class HistorySerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.user.username', read_only=True)
    class Meta:
        model = History
        fields = (
            'id',
            'source_id',
            'author',
            'date_created',
            'longitude',
            'latitude',
            'd_pathogen_pollution',
            'd_inorganic_pollution',
            'd_organic_pollution',
            'd_macroscopic_pollution',
            'd_thermal_pollution',
            'd_climate_condition',
            'd_depletion_risk',
            'd_stress',
         )
