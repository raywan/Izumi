from django.forms import widgets
from rest_framework import serializers
from api.models import Source, Event

class SourceSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.user.username', read_only=True)
    class Meta:
        model = Source
        fields = (
            'author',
            'date_created',
            'last_update',
            'longitude',
            'latitude',
            'source_type',
            'pathogen_pollution',
            'inorganic_pollution',
            'organic_pollution',
            'macroscopic_pollution',
            'thermal_pollution',
         )
